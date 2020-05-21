import json
import Algorithmia
import spacy
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, KeywordsOptions
from Robos import stateRobot
import random


# Retorna o conteudo do Wikipedia
async def fetchContentFromWiki(content):
    entrada = {"articleName": content, "lang": 'pt'}
    with open(r'C:\Users\Marcos\Documents\Credenciais\credenciais.json') as json_file:
        dados = json.load(json_file)
        client = Algorithmia.client(dados["Algorithmia"])
    wikiAlgorithm = client.algo('web/WikipediaParser/0.1.2')
    wikiAlgorithm.set_options(timeout=300)
    wikiContent = wikiAlgorithm.pipe(entrada).result
    return wikiContent['content']


# Limpa o conteudo extraido
def sanitizeContent(bruteVar):
    for character in ("!@#$%*()<>:|/?=+~[]\""):
        bruteVar = bruteVar.replace(character, "")
    cleanVar = bruteVar.replace("\n", '')
    return cleanVar


# Retorna todas as sentenças enontradas nos textos
def breakContentIntoSentences(cleanVar):
    nlp = spacy.load('pt_core_news_sm')
    sent = nlp(cleanVar)
    doc = []
    for sent in sent.sents:
        doc.append({'Sentence': str(sent)})
    return doc


# Integra o Watson e retorna um conjunto de palavras chave para
# cada sentença fornecida
def cleanResponse(response):
    lista = ['usage', 'language']
    lista2 = ['relevance', 'count']
    for i in lista:
        del response[i]
    for i in range(len(response['keywords'])):
        dictionary = response['keywords'][i]
        for j in lista2:
            del dictionary[j]
    return response


# Faz o ligin com o Watson e devolve as keywords
async def fethWatsonAndReturnKeywords(doc):
    # Autenticação de usuario
    with open(r'C:\Users\Marcos\Documents\Credenciais\credenciais.json') as json_file:
        dados = json.load(json_file)
        watson_apiKey = dados["Watson_apikey"]
        watson_URL = dados["Watson_url"]
    authenticator = IAMAuthenticator(watson_apiKey)
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        version='2019-07-12',
        authenticator=authenticator
    )
    natural_language_understanding.set_service_url(watson_URL)
    #result = random.sample(range(0,len(doc)), 7)
    keyInformation = []
    for index in range(7):
        response = natural_language_understanding.analyze(
            text=doc[index]['Sentence'],
            features=Features(keywords=KeywordsOptions(sentiment=False, emotion=False, limit=10)),
            language='pt').get_result()
        clean_dictionary = cleanResponse(response)
        info = dict(doc[index], **clean_dictionary)
        keyInformation.append(info)
    return keyInformation


# Ativa o robo de texto
async def ActivateTextBoot():
    content = stateRobot.load()

    bruteVar = await fetchContentFromWiki(content=content["SeachTerm"])
    cleanVar = sanitizeContent(bruteVar=bruteVar)
    doc = breakContentIntoSentences(cleanVar=cleanVar)
    keyInformation = await fethWatsonAndReturnKeywords(doc=doc)
    content['Informations'] = keyInformation

    stateRobot.save(content=content)

import Algorithmia
import spacy
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, KeywordsOptions


def fetchContentFromWiki(term):
    entrada = {"articleName": term, "lang": 'pt'}

    f = open(r'C:\Users\Marcos\Documents\Credenciais\Algorithmia.txt')
    client = Algorithmia.client(f.read())
    f.close()

    wikiAlgorithm = client.algo('web/WikipediaParser/0.1.2')
    wikiAlgorithm.set_options(timeout=300)
    wikiContent = wikiAlgorithm.pipe(entrada).result
    return wikiContent['content']


def sanitizeContent(bruteVar):
    for character in "!@#$%*()<>:|/?=+~[]":
        bruteVar = bruteVar.replace(character, "")
    cleanVar = bruteVar.replace("\n", '')
    return cleanVar


def breakContentIntoSentences(cleanVar):
    nlp = spacy.load('pt_core_news_sm')
    sent = nlp(cleanVar)
    doc = []
    for sent in sent.sents:
        doc.append(str(sent))
    return doc


def fethWatsonAndReturnKeywords(doc):
    # Autenticação de usuario
    authenticator = IAMAuthenticator('HZWB8HPGlrXgLPOeZN9kTPpXMK2ok0EAqGdLv9dcrIsH')
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        version='2019-07-12',
        authenticator=authenticator
    )
    natural_language_understanding.set_service_url(
        'https://api.eu-gb.natural-language-understanding.watson.cloud.ibm.com/instances/ed1586a0-30bb-4312-9206'
        '-97c8c883d30b')
    keyInformation = []
    for index in range(3):
        response = natural_language_understanding.analyze(
            text=doc[index],
            features=Features(keywords=KeywordsOptions(sentiment=False, emotion=False, limit=5)),
            language='pt').get_result()
        keyWordsTMP = response['keywords']
        keyWords = []
        for i in range(len(keyWordsTMP)):
            keyWords.append(keyWordsTMP[i]['text'])
        keyInformation.append([{'sentence': doc[index]},keyWords])
    return keyInformation

def ActivateBootText(bruteTerm):
    bruteVar = fetchContentFromWiki(bruteTerm)
    cleanVar = sanitizeContent(bruteVar)
    doc = breakContentIntoSentences(cleanVar)
    keyInformation = fethWatsonAndReturnKeywords(doc=doc)
    for i in range(len(keyInformation)):
        print(keyInformation[i])

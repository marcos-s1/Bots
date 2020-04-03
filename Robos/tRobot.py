import Algorithmia
import spacy

def fetchContentFromWiki(term):
    entrada = {"articleName": term, "lang": 'pt'}
    client = Algorithmia.client('simpH1sdB8f0kKgeKK+zp5KfmEE1')
    wikiAlgorithm = client.algo('web/WikipediaParser/0.1.2')
    wikiAlgorithm.set_options(timeout=300)
    wikiContent = wikiAlgorithm.pipe(entrada).result
    return wikiContent['content']


def sanitizeContent(bruteVar):
    for character in "!@#$%*()<>:|/?=+~[]":
        bruteVar =  bruteVar.replace(character,"")
    cleanVar = bruteVar.replace("\n",'')
    return cleanVar

def breakContentIntoSentences(cleanVar):
    nlp = spacy.load('pt_core_news_sm')
    sent =nlp(cleanVar)
    doc = []
    for sent in sent.sents:
        doc.append([sent, [sent.ents],[]])
    return doc

def ActivateBootText(bruteTerm):
    bruteVar = fetchContentFromWiki(bruteTerm)
    cleanVar = sanitizeContent(bruteVar)
    doc = breakContentIntoSentences(cleanVar)
    print(doc[1])


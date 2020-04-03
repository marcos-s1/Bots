import Algorithmia
import spacy

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
        doc.append([sent, [sent.ents], []])
    return doc


def ActivateBootText(bruteTerm):
    bruteVar = fetchContentFromWiki(bruteTerm)
    cleanVar = sanitizeContent(bruteVar)
    doc = breakContentIntoSentences(cleanVar)
    print(doc[1])

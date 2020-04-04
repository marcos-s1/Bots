'''import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, KeywordsOptions

authenticator = IAMAuthenticator('HZWB8HPGlrXgLPOeZN9kTPpXMK2ok0EAqGdLv9dcrIsH')
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2019-07-12',
    authenticator=authenticator
)

natural_language_understanding.set_service_url('https://api.eu-gb.natural-language-understanding.watson.cloud.ibm.com/instances/ed1586a0-30bb-4312-9206-97c8c883d30b')

response = natural_language_understanding.analyze(
    text='Michael Joseph Jackson (Gary, 29 de agosto de 1958 — Los Angeles, 25 de junho de 2009) foi um cantor, compositor e dançarino estadunidense. Apelidado de "Rei do Pop", ele é considerado uma das figuras culturais mais importantes do século XX e um dos maiores artistas da história da música. As contribuições de Jackson para a música, a dança e a moda, juntamente com a divulgação de sua vida pessoal, fizeram dele uma figura global na cultura popular por mais de quatro décadas.',
    features=Features(keywords=KeywordsOptions(sentiment=False,emotion=False,limit=2))).get_result()

print(response)      '''
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, KeywordsOptions
doc = ['Michael Joseph Jackson (Gary, 29 de agosto de 1958 — Los Angeles, 25 de junho de 2009) foi um cantor, compositor e dançarino estadunidense. '
       'Apelidado de "Rei do Pop", ele é considerado uma das figuras culturais mais importantes do século XX e um dos maiores artistas da história da música.',
       'As contribuições de Jackson para a música, a dança e a moda, juntamente com a divulgação de sua vida pessoal, '
       'fizeram dele uma figura global na cultura popular por mais de quatro décadas.']
# Autenticação de usuario
authenticator = IAMAuthenticator('HZWB8HPGlrXgLPOeZN9kTPpXMK2ok0EAqGdLv9dcrIsH')
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2019-07-12',
    authenticator=authenticator
)
natural_language_understanding.set_service_url(
    'https://api.eu-gb.natural-language-understanding.watson.cloud.ibm.com/instances/ed1586a0-30bb-4312-9206-97c8c883d30b')
informations = []
for i in doc:
    response = natural_language_understanding.analyze(
        text=i,
        features=Features(keywords=KeywordsOptions(sentiment=False, emotion=False, limit=2))).get_result()
    informations.append(response)
print(informations)

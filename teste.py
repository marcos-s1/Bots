import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, CategoriesOptions

authenticator = IAMAuthenticator("HZWB8HPGlrXgLPOeZN9kTPpXMK2ok0EAqGdLv9dcrIsH")
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2019-07-12',
    authenticator=authenticator
)

natural_language_understanding.set_service_url("https://api.eu-gb.natural-language-understanding.watson.cloud.ibm.com/instances/ed1586a0-30bb-4312-9206-97c8c883d30b")

response = natural_language_understanding.analyze(
    text='Meu nome é marcos', features=Features(categories=CategoriesOptions(limit=3))
).get_result()

print(json.dumps(response, indent=2))
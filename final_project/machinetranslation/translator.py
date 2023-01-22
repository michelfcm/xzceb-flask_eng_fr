import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version = os.environ['version']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=version,
    authenticator=authenticator
)

language_translator.set_service_url(url)

# languages = language_translator.list_languages().get_result()
# print(json.dumps(languages, indent=2))

def englishToFrench(englishText):
    translation = language_translator.translate(
    englishText,
    model_id='en-fr').get_result()
    return (translation['translations'][0]['translation'])

print(englishToFrench('United States of America'))

def frenchToEnglish(frenchText):
    translation = language_translator.translate(
    frenchText,
    model_id='fr-en').get_result()
    return (translation['translations'][0]['translation'])

print(frenchToEnglish("États-Unis d'Amérique"))

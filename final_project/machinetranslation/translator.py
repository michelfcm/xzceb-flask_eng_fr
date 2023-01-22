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

def englishToFrench(englishText):
    if(type(englishText) == str):
        translation = language_translator.translate(
        englishText,
        model_id='en-fr').get_result()
        frenchText = translation['translations'][0]['translation']
        result = frenchText if frenchText != englishText.capitalize() else 'No translation'
    else:
        result = 'No translation'
    return result 

def frenchToEnglish(frenchText):
    if(type(frenchText) == str):
        translation = language_translator.translate(
        frenchText,
        model_id='fr-en').get_result()
        englishText = translation['translations'][0]['translation']
        result = englishText if englishText != frenchText.capitalize() else 'No translation'
    else:
        result = 'No translation'
    return result

"""
Module to tranlate words and phrases
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
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

def english_to_french(english_text):
    """
    This function translates english to french
    """
    if isinstance(english_text, str):
        translation = language_translator.translate(
        english_text,
        model_id='en-fr').get_result()
        french_text = translation['translations'][0]['translation']
        result = french_text if french_text != english_text.capitalize() else english_text + ' (No translation)'
    else:
        result = str(english_text) + ' (No translation)'
    return result

def french_to_english(french_text):
    """
    This function translates french to english
    """
    if isinstance(french_text, str):
        translation = language_translator.translate(
        french_text,
        model_id='fr-en').get_result()
        english_text = translation['translations'][0]['translation']
        result = english_text if english_text != french_text.capitalize() else french_text + ' (No translation)'
    else:
        result = str(french_text) + ' (No translation)'
    return result
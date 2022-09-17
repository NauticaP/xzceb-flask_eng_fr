import json
import os 
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('nciFuLEyB_lUFZgmiiRdk5YBUffua59FXApyLm9dwhS1')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com/instances/16bc23ef-e355-484e-a1d6-a86b869c59ca')


def englishToFrench(englishText):
    frenchText=language_translator.translate(
        text=englishText,
        model_id='en-fr'
    ).get_result()
    return frenchText.get("translations")[0].get("translation")

def frenchToEnglish(frenchText):
    englishText=language_translator.translate(
        text=frenchText,
        model_id='fr-en'
    ).get_result()
    return englishText.get("translations")[0].get("translation")

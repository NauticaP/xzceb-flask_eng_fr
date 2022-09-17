from machinetranslation import translator
from flask import Flask , render_template, request

import json

app=Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench(englishText):
    frenchText=language_translator.translate(
        text=englishText,
        model_id='en-fr'
    ).get_result()
    return frenchText.get("translations")[0].get("translation")

@app.route("/frenchToEnglish")
def frenchToEnglish(frenchText):
    englishText=language_translator.translate(
        text=frenchText,
        model_id='fr-en'
    ).get_result()
    return englishText.get("translations")[0].get("translation")

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

if __name__=="__main__":
    app.run(host="0.0.0.0", port=8080)
import requests
import json

def sentiment_analyzer(text_to_analyze):

    url = "https://sn-watson-sentiment.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict"

    headers = {
        "grpc-metadata-mm-model-id": "sentiment_aggregated-workflow_lang_en_stock"
    }

    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(url, json=input_json, headers=headers)

    formatted_response = json.loads(response.text)

    label = formatted_response["documentSentiment"]["label"]
    score = formatted_response["documentSentiment"]["score"]

    return {
        "label": label,
        "score": score
    }


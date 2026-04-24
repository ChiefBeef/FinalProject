import json
import requests


def emotion_detector(text_to_analyze):
    url = ('https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict')
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header, timeout=10)
    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        anger = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness = formatted_response['emotionPredictions'][0]['emotion']['sadness']
        emotions_list = [anger, disgust, fear, joy, sadness]
        emotion_labels = ['anger', 'disgust', 'fear', 'joy', 'sadness']
        dominant_emotion = 0
        dom_emote_label = ' '
        index = 0
        for item in emotions_list:
            if item > dominant_emotion:
                dominant_emotion = item
                dom_emote_label = emotion_labels[index]
            index += 1
    if response.status_code == 400:
        anger = None
        disgust = None
        fear = None
        joy = None
        sadness = None
        dom_emote_label = None
    return {'anger': anger, 'disgust': disgust, 'fear': fear, 'joy': joy, 'sadness': sadness, 'dominant emotion': dom_emote_label}
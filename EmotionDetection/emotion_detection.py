import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers = header)
    formatted_response = json.loads(response.text)
    if response.status_code == 200:
        anger = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness = formatted_response['emotionPredictions'][0]['emotion']['sadness']
        emotions = {
                    'anger': anger,
                    'disgust': disgust,
                    'fear': fear,
                    'joy': joy,
                    'sadness': sadness      
                }
        max_key = max(emotions, key = lambda k: emotions[k])
        emotions['dominant_emotion'] = max_key
        return emotions
    elif response.status_code == 400:
        return {
                    'anger': None, 'disgust': None, 'fear': None, 'joy': None,
                    'sadness': None, 'dominant_emotion': None      
                }
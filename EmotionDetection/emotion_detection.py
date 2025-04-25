import requests #import requests library
import json #import json library

def emotion_detector(text_to_analyse):
    '''accepts a text as input and returns emotion description and a dominant emotion as a json. calls watson emotion detection feature '''
    # URL of the emotion analysis service
    url='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Custom header specifying the model ID for the emotion analysis service
    header={"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Constructing the request payload in the expected format
    myobj={ "raw_document": { "text": text_to_analyse } }
    # Sending a POST request to the emotion analysis API
    response = requests.post(url, json = myobj, headers=header)
    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)
    # If the response status code is 400, set values to None
    if response.status_code == 400:
        formatted_response = { 'anger': None,
                             'disgust': None,
                             'fear': None,
                             'joy': None,
                             'sadness': None,
                             'dominant_emotion': None }
    else:
        # Parsing the JSON response from the API
        res=json.loads(response.text)
        formatted_response = res['emotionPredictions'][0]['emotion']
        # Defining the dominant emotion
        dominant_emotion=max(formatted_response,key=formatted_response.get)
        formatted_response['dominant_emotion']=dominant_emotion
	    # Returning a dictionary containing emotion analysis results
    return formatted_response

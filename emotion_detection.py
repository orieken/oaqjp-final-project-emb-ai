import requests

# URL: 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
# Headers: {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
# Input json: { "raw_document": { "text": text_to_analyse } }

url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}


# def emotion_detector(text_to_analyse):
#   payload = { "raw_document": { "text": text_to_analyse } }
#   response = requests.post(url, headers=headers, json=payload)
#   return response.json()

def emotion_detector(text_to_analyse):
  payload = { "raw_document": { "text": text_to_analyse } }
  response = requests.post(url, headers=headers, json=payload)
  json = response.json()
  anger_score = json['emotionPredictions'][0]['emotions']['anger']
  disgust_score = json['emotionPredictions'][0]['emotions']['disgust']
  fear_score = json['emotionPredictions'][0]['emotions']['fear']
  joy_score = json['emotionPredictions'][0]['emotions']['joy']
  sadness_score = json['emotionPredictions'][0]['emotions']['sadness']

  emotions = json['emotionPredictions'][0]['emotions']
  high_score = max(emotions, key=emotions.get)

  return {
    'anger': anger_score,
    'disgust': disgust_score,
    'fear': fear_score,
    'joy': joy_score,
    'sadness': sadness_score,
    'dominant_emotion': high_score
  }
    
# {'emotionPredictions': [{'emotion': {'anger': 0.01364663, 'disgust': 0.0017160787, 'fear': 0.008986978, 'joy': 0.9719017, 'sadness': 0.055187024}, 'target': '', 'emotionMentions': [{'span': {'begin': 0, 'end': 27, 'text': 'I love this new technology.'}, 'emotion': {'anger': 0.01364663, 'disgust': 0.0017160787, 'fear': 0.008986978, 'joy': 0.9719017, 'sadness': 0.055187024}}]}], 'producerId': {'name': 'Ensemble Aggregated Emotion Workflow', 'version': '0.0.1'}}    # 

# r = emotion_detector("I love this new technology.")
# print(r)
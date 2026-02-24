from flask import Flask, request, jsonify
from src.EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
  print(request.json)
  text = request.json['text']

  result = emotion_detector(text)
  return jsonify(result)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5090, debug=True)

''' Emotion Detector App (using Flask) '''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("EmotionDetector")

@app.route("/emotionDetector")
def sent_analyzer():
    ''' sents text to analaze and receives answer'''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    # Return a formatted string with the sentiment label and score
    if dominant_emotion is None:
        # Empty request and empty output
        response_text="Invalid Input! Please try again."
    else:
        response_text=f"For the given statement, the system response is 'anger': {anger},"\
           f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}"\
           f" and 'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
    return response_text

@app.route("/")
def render_index_page():
    ''' home page of the app'''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
    
from flask import Flask, render_template, request
from emotion_detection import emotion_detector
app = Flask("Emotion Detection")
app.debug = True

@app.route("/emotionDetector", methods=['GET', 'POST'])
def detect_route():
    if request.method == 'POST':
        data = request.get_json(silent=True)
        text_to_analyze = None
        if data:
            text_to_analyze = data.get('textToAnalyze') 
        if not text_to_analyze:
            text_to_analyze = request.form.get('textToAnalyze')
    else:
        text_to_analyze = request.args.get('textToAnalyze')
    
    response = emotion_detector(text_to_analyze)
    anger = response.get('anger')
    disgust = response.get('disgust')
    fear = response.get('fear')
    joy = response.get('joy')
    sadness = response.get('sadness')
    dominant_emotion = response.get('dominant emotion')
    if dominant_emotion != None:
        return (f"For the given statement, the system response is 'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. The dominant emotion is <b>{dominant_emotion}</b>.")
    else:
        return "<b>Invalid text! Please try again!</b>"
@app.route("/")
def render_index_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
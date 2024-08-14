from flask import Flask, render_template, request, jsonify
from analyze import get_response_based_on_emotion, emotion_list

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', emotions=emotion_list)

@app.route('/get_response', methods=['POST'])
def get_response():
    data = request.get_json()
    emotion = data.get('emotion')
    user_input = data.get('user_input')
    
    if emotion and user_input:
        response = get_response_based_on_emotion(emotion, user_input)
        return jsonify({"response": response})
    
    return jsonify({"response": "Please provide valid inputs."}), 400

if __name__ == "__main__":
    app.run(debug=True)

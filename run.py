from flask import Flask, render_template, request, jsonify
from app.chat import rag_chain
from app.recommendation_model import predict
from app.pd_model import predict_disease
from io import BytesIO
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello World!"
@app.route('/recommend/get', methods=['POST'])
def recommend():
    try:
        data = request.get_json(force=True)
        features = data.get('features')
        if not isinstance(features, list) or len(features) != 7:
            return jsonify({'error': 'Invalid input. Must provide exactly 7 feature values.'}), 400
        return jsonify({'prediction': str(predict([features])[0])})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
@app.route("/chat/get", methods=["POST"])  # Change to POST request
def get_bot_response():
    data = request.json  # Get JSON data from the request
    userText = data.get('msg')  # Access the 'msg' field
    if userText:
        response = rag_chain.invoke(userText)
        return jsonify({"response": response})  # Return JSON response
    else:
        return jsonify({"error": "No message received."}), 400  # Return error response

@app.route("/plant/get", methods=['POST'])
def classify_disease():
    try:
        # Check if the request contains a file
        if 'image' not in request.files:
            return jsonify({'error': 'No file part'}), 400

        file = request.files['image']

        # Check if a file was actually selected
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        # Read the image file
        image = file.read()

        # Process the image and get the prediction
        # Wrap the image data in a BytesIO object if needed
        image_stream = BytesIO(image)
        prediction = predict_disease(image_stream)

        # Return the prediction as JSON
        return jsonify({'prediction': str(prediction[0])})

    except Exception as e:
        # Return an error message in case of an exception
        return jsonify({'error': str(e)}), 500
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
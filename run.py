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

        image = file.read()
        image_stream = BytesIO(image)
        prediction = predict_disease(image_stream)
        def recommend_action(disease):
          if disease.find("healthy") != -1:
            return "ဤအပင်သည် ကျန်းမာပါသည်။"
          else:
            return return f"""ဤ{disease}ရောဂါကို အောက်ပါအဆင့်များဖြင့် ဖယ်ရှားနိုင်သည်။
                  ၁။ရောဂါကူးစက်ထားသောအပိုင်းများကို ဖယ်ရှားပေးခြင်းနှင့် အခင်းကို သန့်ရှင်းရေးလုပ်ပေးခြင်း
                  ၂။မှိုသတ်ဆေးများအသုံးပြုခြင်း
                  ၃။အခက်ချိုင်ခြင်း
                  ၄။လုံလောက်စွာ ရေလောင်းပေးခြင်း
                  ၅။ရောဂါလက္ခဏာများကို ပုံမှန် စစ်ဆေးပေးခြင်း
                  ပြုလုပ်ပုံအသေးစိတ်အား စက်ရုပ်ကို မေးမြန်းပါ။"""
        recommend_text=recommend_action(str(prediction[0]))
        return jsonify({'prediction': str(prediction[0]),'confidence':str(prediction[1]),'recommend_text':str(recommend_text)})

    except Exception as e:
        # Return an error message in case of an exception
        return jsonify({'error': str(e)}), 500
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import pandas as pd
import joblib
import tensorflow as tf
from PIL import Image
import numpy as np
import json

app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)

model1 = joblib.load("SoilClassifier.pkl")
price_model = joblib.load("Prices.pkl")  
model2 = tf.keras.models.load_model("diseases.h5")  

@app.route('/')
def home():
    return render_template('main_index.html')

@app.route('/Soilindex')
def soil_index():
    return render_template('Soilindex.html')

@app.route('/Priceindex')
def price_index():
    return render_template('priceindex.html')

@app.route('/diseaseIndex')
def disease_index():
    return render_template('diseaseindex.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        input_df = pd.DataFrame([data])
        prediction = model1.predict(input_df)

        return jsonify({
            'success': True,
            'prediction': str(prediction[0])  
        })
    except Exception as e:
        print("Error during prediction:", e)  
        return jsonify({
            'success': False,
            'error': str(e)
        })

@app.route('/predict1', methods=['POST'])
def predict1():
    try:
        data = request.json
        input_df = pd.DataFrame([data])
        y_pred = price_model.predict(input_df)[0]

        min_rate, max_rate, avg_rate = y_pred

        return jsonify({
            'success': True,
            'min': min_rate,
            'max': max_rate,
            'avg': avg_rate
        })
    except Exception as e:
        print("Error during prediction:", e)
        return jsonify({
            'success': False,
            'error': str(e)
        })

with open('label_list.json', 'r') as f:
    label_list = json.load(f)

@app.route('/predict2', methods=['POST'])
def predict2():
    try:
        if 'image' not in request.files:
            return jsonify({'success': False, 'error': 'No image file provided'})

        file = request.files['image']
        img = Image.open(file.stream).convert('RGB')
        img = img.resize((224, 224))
        img_array = np.array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        prediction = model2.predict(img_array)
        predicted_index = np.argmax(prediction, axis=1)[0]

        predicted_label = label_list[predicted_index]
        cleaned_label = predicted_label.split("___")[1] if "___" in predicted_label else predicted_label

        return jsonify({
            'success': True,
            'prediction': cleaned_label
        })

    except Exception as e:
        print("Error during prediction:", e)
        return jsonify({'success': False, 'error': str(e)})


          
if __name__ == '__main__':
    app.run(port=5000, debug=True)


from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pickle
import numpy as np
import os

app = Flask(__name__)
CORS(app, resources={r"/predict": {"origins": "*"}})

with open("crop_rf_model.pkl", "rb") as f:
    crop_model = pickle.load(f)

with open("Label_rf_model.pkl", "rb") as f:
    label_encoder = pickle.load(f)

@app.route("/")
def index():
    return "Crop Recommendation API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        features = np.array([[
            float(data["N"]), float(data["P"]), float(data["K"]),
            float(data["temperature"]), float(data["humidity"]),
            float(data["ph"]), float(data["rainfall"])
        ]])
        prediction = crop_model.predict(features)
        crop_name = label_encoder.inverse_transform(prediction)[0]
        return jsonify({"success": True, "crop": crop_name})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

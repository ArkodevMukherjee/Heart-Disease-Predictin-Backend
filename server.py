from flask import Flask
from flask import request,jsonify
from Model.main import load_model
from flask_cors import CORS
import pandas as pd


app = Flask(__name__)
CORS(app)


@app.route('/heart-disease',methods=['POST'])
def predict_heart_disease():
    age = int(request.json.get("age"))
    sex = int(request.json.get("sex"))
    chest_pain_type = int(request.json.get("chest pain type"))
    resting_bp_s = int(request.json.get("resting bp s"))
    cholesterol = int(request.json.get("cholesterol"))
    fasting_blood_sugar = int(request.json.get("fasting blood sugar"))
    resting_ecg = int(request.json.get("resting ecg"))
    max_heart_rate = int(request.json.get("max heart rate"))
    exercise_angina = int(request.json.get("exercise angina"))
    oldpeak = int(request.json.get("oldpeak"))
    ST_slope = int(request.json.get("ST slope"))

    data = pd.DataFrame([{
    "age": age,
    "sex": sex,
    "chest pain type": chest_pain_type,
    "resting bp s": resting_bp_s,
    "cholesterol": cholesterol,
    "fasting blood sugar": fasting_blood_sugar,
    "resting ecg": resting_ecg,
    "max heart rate": max_heart_rate,
    "exercise angina": exercise_angina,
    "oldpeak": oldpeak,
    "ST slope": ST_slope
    }])


    prediction = load_model(data)

    if(prediction==0):
        return jsonify({"message":0})
    
    else:
        return jsonify({"message":1})
    



if __name__ == "__main__":
    app.run(debug=True)
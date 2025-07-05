import pandas as pd
import sklearn
import cloudpickle



def load_model(data:pd.DataFrame):
   with open("heart-disease(1).pkl", "rb") as f:
    pipeline = cloudpickle.load(f)
    prediction = pipeline.predict(data)
    return prediction[0]

if __name__ == "main__":
    test_data = pd.DataFrame([{
    "age": 42,
    "sex": 1,
    "chest pain type": 1,
    "resting bp s": 155,
    "cholesterol": 310,
    "fasting blood sugar": 0,
    "resting ecg": 1,
    "max heart rate": 170,
    "exercise angina": 0,
    "oldpeak": 3.5,
    "ST slope": 2
}])
    print(load_model(test_data))
    
    

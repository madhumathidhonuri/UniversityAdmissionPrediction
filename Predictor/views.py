from django.shortcuts import render
import joblib
import os
import numpy as np

MODEL_FILE_PATH = os.path.join(os.path.dirname(__file__), 'admission_model.joblib')

try:
    MODEL = joblib.load(MODEL_FILE_PATH)
    print(f"Model loaded successfully from {MODEL_FILE_PATH}")
except FileNotFoundError:
    print(f"Error: Model file not found at {MODEL_FILE_PATH}")
    MODEL = None
except Exception as e:
    print(f"Error loading model: {e}")
    MODEL = None

def home(request):
    return render(request, 'predictor/index.html')

def predict_chance(request):
    if request.method == 'POST' and MODEL:
        try:
            gre = float(request.POST['gre'])
            toefl = float(request.POST['toefl'])
            rating = float(request.POST['rating'])
            sop = float(request.POST['sop'])
            lor = float(request.POST['lor'])
            cgpa = float(request.POST['cgpa'])
            research = float(request.POST['research'])

            features = np.array([[gre, toefl, rating, sop, lor, cgpa, research]])
            prediction = MODEL.predict(features)
            
            # The model gives a result between 0.0 and 1.0
            result_percentage = round(prediction[0] * 100, 2)
            
            if result_percentage < 0:
                result_percentage = 0
            elif result_percentage > 100:
                result_percentage = 100

            context = {
                'prediction_text': f"Your Predicted Chance of Admission is:",
                'prediction_value': f"{result_percentage}%",
                'form_data': request.POST 
            }
            return render(request, 'predictor/result.html', context)

        except (KeyError, TypeError, ValueError):
            error_context = {
                'error_message': "Invalid input. Please fill all fields correctly."
            }
            return render(request, 'predictor/index.html', error_context)
    return render(request, 'predictor/index.html')
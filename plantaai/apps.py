# plantaai/apps.py
from django.apps import AppConfig
import joblib
import os

class PlantaaiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'plantaai'
    
    # Variables to hold our loaded model and features
    model = None
    features = None

    def ready(self):
        # Load the model and feature names when the app is ready
        # The paths below assume you place your joblib files in plantaai/planta_model/
        model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'planta_model', 'planta_random_forest_model.joblib')
        features_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'planta_model', 'planta_feature_names.joblib')

        if os.path.exists(model_path) and os.path.exists(features_path):
            self.model = joblib.load(model_path)
            self.features = joblib.load(features_path)
            print("ML Models loaded successfully into PlantaaiConfig.")
        else:
            print("ML Model files not found. Check paths.")


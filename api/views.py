from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pandas as pd
from django.apps import apps
from .serializers import PredictionInputSerializer
# from plantaai.models import PredictionHistory # Not saving to DB in MVP view for simplicity

class PredictYieldView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = PredictionInputSerializer(data=request.data)
        if serializer.is_valid():
            # Get the validated input data as a dictionary
            input_data = serializer.validated_data
            
            # Load the model and features from the AppConfig
            PlantaaiConfig = apps.get_app_config('plantaai')
            model = PlantaaiConfig.model
            features = PlantaaiConfig.features

            if model and features is not None:
                # Convert input dictionary to a Pandas DataFrame instance
                input_df = pd.DataFrame([input_data])
                
                # Ensure input columns match model's expected features (reorder and add missing dummy cols as 0)
                input_df = input_df.reindex(columns=features, fill_value=0)
                
                # Make the prediction
                prediction = model.predict(input_df)[0] # get the single prediction value
                
                # Return the result in a clean JSON format
                return Response({
                    'predicted_yield_kg': round(prediction, 2),
                    'recommendation_text': 'Based on our analysis, the recommended variety is suitable for your inputs.'
                }, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'ML model not loaded.'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


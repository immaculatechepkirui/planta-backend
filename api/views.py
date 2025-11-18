from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions
import pandas as pd
from django.apps import apps
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from .serializers import PredictionInputSerializer, UserRegistrationSerializer, PredictionHistorySerializer
from plantaai.models import PredictionHistory 

class PredictYieldView(APIView):
    permission_classes = [permissions.IsAuthenticated] 

    def post(self, request, *args, **kwargs):
        serializer = PredictionInputSerializer(data=request.data)
        if serializer.is_valid():
            input_data = serializer.validated_data
            
            PlantaaiConfig = apps.get_app_config('plantaai')
            model = PlantaaiConfig.model
            features = PlantaaiConfig.features

            if model and features is not None:
                input_df = pd.DataFrame([input_data])
                input_df = input_df.reindex(columns=features, fill_value=0)
                prediction = model.predict(input_df)[0]
                
                PredictionHistory.objects.create(
                    user=request.user,
                    predicted_yield_kg=prediction,
                    recommended_variety='Variety TBD (Dynamically generate this later)',
                    **input_data 
                )
                
                return Response({
                    'predicted_yield_kg': round(prediction, 2),
                    'recommendation_text': 'Based on our analysis, the recommended variety is suitable for your inputs.'
                }, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'ML model not loaded.'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SignupView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user_id': user.pk,
                'username': user.username,
            }, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response({'success': 'Successfully logged out.'}, status=status.HTTP_200_OK)


class ConversationListView(generics.ListAPIView):
    serializer_class = PredictionHistorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return PredictionHistory.objects.filter(user=self.request.user).order_by('-prediction_date')
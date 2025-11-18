from django.urls import path
from .views import PredictYieldView

urlpatterns = [
    path('predict/', PredictYieldView.as_view(), name='predict-yield'),
]

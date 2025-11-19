from django.urls import path, include 
from .views import ConversationListView 
from .views import ConversationListView, PredictYieldView, SignupView, LoginView, LogoutView, UserMeView
urlpatterns = [
    path('predict/', PredictYieldView.as_view(), name='predict-yield'),
    path('auth/me/', UserMeView.as_view(), name='user-me'),
    path('auth/signup/', SignupView.as_view(), name='account-signup'),
    path('auth/login/', LoginView.as_view(), name='account-login'),
    path('auth/logout/', LogoutView.as_view(), name='account-logout'),
    path('conversations/', ConversationListView.as_view(), name='conversation-list'),
] 

from django.urls import path
from .views import RegisterView  
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # Use RegisterView as class-based view
    path('get-token/', obtain_auth_token, name='get-token'),
]


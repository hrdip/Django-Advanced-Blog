from django.urls import path
from . import views
#from rest_framework.authtoken.views import ObtainAuthToken
app_name = "api-v1"

urlpatterns = [
    path('registration/', views.RegistrationApiView.as_view(), name='registeation'),
    # general auth just redirect token
    # path('token/login', ObtainAuthToken.as_view(), name='token-login'),
    # custom auth class
    path('token/login/', views.CustomObtainAuthToken .as_view(), name='token-login'),

 ] 
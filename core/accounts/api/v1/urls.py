from django.urls import path
from . import views
#from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

app_name = "api-v1"

urlpatterns = [
    # Registration
    path('registration/', views.RegistrationApiView.as_view(), name='registeation'),
    
    # Login
    # general auth just redirect token
    # path('token/login', ObtainAuthToken.as_view(), name='token-login'),
    # custom auth class
    path('token/login/', views.CustomObtainAuthToken .as_view(), name='token-login'),
    path('token/logout/', views.CustomDiscardAuthToken .as_view(), name='token-logout'),
    # general jwt just redirect access and refresh
    # path('jwt/create/', TokenObtainPairView.as_view(), name='jwt-create'),
    # custom jwt class
    path('jwt/create/', views.CustomTokenObtainPairView.as_view(), name='jwt-create'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='jwt-refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(),name='jwt-verify'),

    # Change password
    path('change-password/', views.ChangePasswordApiView.as_view(), name='change-password'),

    # Reset password
 ] 
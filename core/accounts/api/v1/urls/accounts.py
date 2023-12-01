from django.urls import path
from .. import views
#from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


urlpatterns = [
    # Registration
    path('registration/', views.RegistrationApiView.as_view(), name='registeation'),
    
    # Test send email to Terminal
    path('test-email/', views.TestEmailSend.as_view(), name='test-email'),
    
    # Activation
    path('activation/confirm/<str:token>', views.ActivationApiView.as_view(), name='activation'),

    # Resend Activation
    path('activation/resend/', views.ActivationResendApiView.as_view(), name='activation-resend'),

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
    path('password-reset/request/',views.RequestPasswordReset.as_view(), name='request-password-reset'),
    path('password-reset/<str:uidb64>/<str:token>/',views.PasswordTokenCheckAPIView.as_view(),name='password-reset'),
    path('password-reset/complete/',views.SetNewPasswordAPIView.as_view(),name='password-reset-complete')
 ] 
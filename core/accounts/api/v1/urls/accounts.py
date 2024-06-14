from django.urls import path
from .. import views


# from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


urlpatterns = [
    # Registration
    path(
        "registration/",
        views.RegistrationApiView.as_view(),
        name="registration",
    ),

    # default auth just redirect token ( ready module )
    # one time generate auth token and always use it. for refresh pages only get this not generated again
    # path('token/login', ObtainAuthToken.as_view(), name='token-login'),

    # custom token authentication
    # class relative with this url doesn't have get function, only have post function, then we can try only in swagger
    path(
        "token/login/",
        views.CustomObtainAuthToken.as_view(),
        name="token-login",
    ),

    # class relative with this url doesn't have get function, only have post function, then we can try only in swagger
    path(
        "token/logout/",
        views.CustomDiscardAuthToken.as_view(),
        name="token-logout",
    ),

    # default jwt, just redirect jwt token_type data (access and refresh)
    # if we want use default class no need to write class in view, then we dont have views. at begin of class name
    # path('jwt/create/', TokenObtainPairView.as_view(), name='jwt-create'),

    # custom jwt, redirect jwt token_type data (access and refresh) and email and user_id
    # custom jwt class for create token
    path(
        "jwt/create/",
        views.CustomTokenObtainPairView.as_view(),
        name="jwt-create",
    ),

    # use default class for refresh jwt token
    # we need refresh token_type, are generated in last jwt token_type
    path("jwt/refresh/", TokenRefreshView.as_view(), name="jwt-refresh"),

    # use default class for verify jwt token
    # check validation access token_type and refresh token_type
    path("jwt/verify/", TokenVerifyView.as_view(), name="jwt-verify"),

    # Test send email to Terminal
    path("test-email/", views.TestEmailSend.as_view(), name="test-email"),

    # Activation
    path(
        "activation/confirm/<str:token>",
        views.ActivationApiView.as_view(),
        name="activation",
    ),

    # Resend Activation
    path(
        "activation/resend/",
        views.ActivationResendApiView.as_view(),
        name="activation-resend",
    ),

    # Change password
    path(
        "change-password/",
        views.ChangePasswordApiView.as_view(),
        name="change-password",
    ),

    # Reset password
    path(
        "reset-password/",
        views.ResetPasswordApiView.as_view(),
        name="reset-password",
    ),

    path(
        "reset-password/<str:token>/",
        views.ResetPasswordCheckTokenApiView.as_view(),
        name="reset-password-check-token",
    ),

    path(
        "reset-password/complete/",
        views.SetNewPasswordAPIView.as_view(),
        name="reset-password-complete",
    ),
]

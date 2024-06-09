from django.urls import path, include
from . import views

app_name = "accounts"

urlpatterns = [
    # rendering page accounting base on django.auth
    path("", include("django.contrib.auth.urls")),
    path("test/", views.test, name="test"),
    path("send-email/", views.send_email, name="send-email"),
    # api accounting urls
    path("api/v1/", include("accounts.api.v1.urls")),
    # django djoser module auth rest_framework
    path("api/v2/", include("djoser.urls")),
    # django djoser module auth rest_framework with jwt token
    path("api/v2/", include("djoser.urls.jwt")),
]

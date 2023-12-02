from django.urls import path
from .views import homeView

app_name = "website"

urlpatterns = [
    path("", homeView, name="home"),
]

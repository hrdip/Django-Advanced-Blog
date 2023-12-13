from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.cache import cache_page
from django.core.cache import cache
import time
from .tasks import sendEmail
import requests

# Create your views here.


def send_email(request):
    sendEmail.delay()
    return HttpResponse("<h1>Done Sending</h1>")


@cache_page(60)
def test(request):
    response = requests.get(
        "https://826db6e7-3cd4-4c80-95ed-c0a144104570.mock.pstmn.io/test/delay/5"
    )
    return JsonResponse(response.json())

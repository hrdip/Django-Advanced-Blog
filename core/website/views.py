from django.shortcuts import render

# Create your views here.

def homeView(request):

    name = "welcome"
    context = {"name": name}
    return render(request,"home.html",context)
from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Post
# Create your views here.

# Function Base View show a template
def indexView(request):
    """
    a function based view to show index page
    """

    name = "hossein"
    context = {"name": name}
    return render(request,"index.html",context)


class IndexView(TemplateView):
    """
    a class based view to show index page
    """
    template_name = "index.html"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "hossein"
        context["posts"] = Post.objects.all()
        return context

''' Function Base View for redirect
from django.shortcuts import redirect
def redirectToHiva(request):
    return redirect('https://hiva-trading.com')
'''

class RedirectToHiva(RedirectView):
    url = 'https://hiva-trading.com'
    
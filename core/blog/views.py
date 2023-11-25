from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic import ListView, DetailView, FormView, CreateView, DeleteView
from .forms import PostForm
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

# Custom Class Base View for TemplateView
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

#Function Base View for RedirectView
'''
from django.shortcuts import redirect
def redirectToHiva(request):
    return redirect('https://hiva-trading.com')
'''

# Custom Class Base View for RedirectView
class RedirectToHiva(RedirectView):
    url = 'https://hiva-trading.com'
    


# Custom Class Base View for ListView
class PostListView(ListView):
    # model = Post
    queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 2
    ordering = '-id'

    ''' 
    insted of model and queryset we can customize with
    this function
    '''
    # def get_queryset(self):
    #     posts = Post.objects.filter(status=True)
    #     return posts


# Custom Class Base View for DetailView
class PostDetailView(DetailView):
    model = Post


# Custom Class Base View for FormView
'''
class PostCreateView(FormView):
    template_name = 'contact.html'
    form_class = PostForm
    success_url = "/blog/post/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    '''

# Custom Class Base View for CreateView
class PostCreateView(CreateView): 
    model = Post
    #fields = ['title', 'content','status', 'category', 'published_date']
    form_class = PostForm
    success_url = '/blog/post/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
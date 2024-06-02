from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    RedirectView,
    ListView,
    DetailView,
    FormView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .forms import PostForm
from .models import Post
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)
from accounts.models import Profile
# Create your views here.


# Function Base View show a template
def indexView(request):
    """
    a function based view to show index page
    """

    name = "hossein"
    context = {"name": name}
    return render(request, "index.html", context)


# Custom Class Base View for TemplateView
class IndexView(TemplateView):
    """
    a class based view to show index page
    """

    template_name = "index.html"

    # pass our argument with this function
    def get_context_data(self, **kwargs):
        # first, go to the mother class and run get_context_data functions, with all arguments that have come with our reques
        context = super().get_context_data(**kwargs)
        # here we can add our arguments with the key-value dictionary
        context["name"] = "hossein"
        context["posts"] = Post.objects.all()
        return context


# Function Base View for RedirectView
"""
from django.shortcuts import redirect
def redirectToHiva(request):
    return redirect('https://hiva-trading.com')
"""


# Custom Class Base View for RedirectView
class RedirectToHiva(RedirectView):
    url = "https://hiva-trading.com"


# Custom Class Base View for ListView
class PostListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    # model = Post
    queryset = Post.objects.all()
    context_object_name = "posts"
    paginate_by = 2
    # if we want to order like this, we must use model or queryset for get objects, if we want to use get_queryset function, we must do ordering into the function not here
    ordering = "-id"
    permission_required = "blog.view_post"

    """
    instead of model and queryset we can customize with
    this function
    """
    # def get_queryset(self):
    #     posts = Post.objects.filter(status=True)
    #     return posts


class PostListApiView(TemplateView):
    template_name = "blog/post_list_api.html"


# Custom Class Base View for DetailView
class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post


# Custom Class Base View for FormView
# show form to user and get data from user and send with email to admin user
"""
class PostCreateView(FormView):
    template_name = 'contact.html'
    # if we want send an email, we can add a function (def send_email(self)) to the form_class we used
    form_class = PostForm
    success_url = "/blog/post/"

    def form_valid(self, form):
        # if we want only save form we need to use this code
        form.save()
        # if we have send_email function in form_class we need to use this code
        form.send_email()
        return super().form_valid(form)
    """


# Custom Class Base View for CreateView
# when the user fills up the form save it on database
class PostCreateView(LoginRequiredMixin, CreateView):
    # this form is filled with the user must be saved on this model on the database
    model = Post
    # fields = ['title', 'content','status', 'category', 'published_date']
    form_class = PostForm
    success_url = "/blog/post/"
    template_name = "blog/post_create.html"

    def form_valid(self, form):
        # Retrieve the Profile instance associated with the current user
        form.instance.author = Profile.objects.get(user=self.request.user)
        return super().form_valid(form)


# Custom Class Base View for UpdateView
class PostEditView(LoginRequiredMixin, UpdateView):
    model = Post
    # fields = ['title', 'content','status', 'category', 'published_date']
    form_class = PostForm
    success_url = "/blog/post/"
    template_name = "blog/post_edit.html"


# Custom Class Base View for DeleteView
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = "/blog/post/"

from django.shortcuts import render
from django.utils import timezone
from .forms import PostForm
from .models import Post
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
)

# Create your views here.

def register(response):
    return render()

def registerPage(request):
    context = {}
    return render(request, 'insta/signup.html', context)

def loginPage(request):
    context = {}
    return render(request, 'insta/login.html', context)

class PostListView(ListView):
    template_name = "insta/post_list.html"
    queryset = Post.objects.all().filter(created_date__lte=timezone.now()).order_by('-created_date')
    context_object_name = 'posts'

class PostCreateView(CreateView):
    template_name = 'insta/post_create.html'
    form_class = PostForm
    queryset = Post.objects.all()
    success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        form.instance.author = self.request.user
        return super().form_valid(form)
class PostDetailView(DetailView):
    template_name = 'insta/post_detail.html'
    queryset = Post.objects.all().filter(created_date__lte=timezone.now())
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Post, id=id_)
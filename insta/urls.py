from django.urls import path, include
# from register import views as v

from . import views
from .views import (
    PostListView,
    PostCreateView,
    PostDetailView, 
)

app_name = 'insta'

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    # path('register/', v.register, name="register"),
    path('login/', views.loginPage, name="login"),
    #local = http://127.0.0.1:8000/
    path('', PostListView.as_view(), name='post_list'),
    path('new/', PostCreateView.as_view(), name='post_create'),
    path('<int:id>', PostDetailView.as_view(), name='post_detail'),
    path('', include("django.contrib.auth.urls")),
]
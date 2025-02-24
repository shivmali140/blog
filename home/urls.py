from django.urls import path
from .views import *

urlpatterns = [
    path("",home,name='home'),
    path("login/", login_view, name="login"),
    path("register/",register,name="register"),
    path("profile/", profile, name="profile"),
    path("logout",logout_view,name="logout"),

    path('<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
    path('new/', BlogCreateView.as_view(), name='blog-create'),
    path('<int:pk>/edit/', BlogUpdateView.as_view(), name='blog-update'),
    path('<int:pk>/delete/', BlogDeleteView.as_view(), name='blog-delete'),
    path("viewProfile/",profile,name="viewProfile")
]
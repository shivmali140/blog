from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from .models import *
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


# Home view
def home(request):
    recentBlogs = Blog.objects.order_by('-date_posted')[:6]

    if request.user.is_authenticated:
        personal_blogs = Blog.objects.filter(author=request.user)
        if not personal_blogs.exists():  # Check if user has blogs
            personal_blogs = None

        # Show login success message only if redirected from login
        if "login_success" in request.GET:
            messages.success(request, "Login successful!")

        return render(request, 'home/home_user.html', {
            'user': request.user,
            'blogs': recentBlogs,
            'personal_blogs': personal_blogs
        })

    return render(request, 'home/home_guest.html', {'blogs': recentBlogs})

# User registration view
def register(request):
    if request.method == "POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")  
    else:
        form = CustomUserForm()
    
    return render(request, "home/register.html", {"form": form})

# user profile view
@login_required
def profile(request):
    personal_blogs = Blog.objects.filter(author__username=request.user.username)
    return render(request, "home/profile.html", {"user": request.user,"personal_blogs":personal_blogs})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()
    
    return render(request, "home/login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect('home')

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'home/blog_detail.html'
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog = self.get_object()
        context['can_edit'] = self.request.user == blog.author  
        return context

class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogForm
    template_name = 'home/blog_form.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BlogUpdateView(UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = 'home/blog_form.html'
    success_url = reverse_lazy('home')

class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'home/blog_delete.html'
    success_url = reverse_lazy('home')

from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from .forms import *
from blog.models import Article
from django.urls import path, reverse_lazy


# def MainPage(request):
#     posts = Article.objects.all()
#     return render(request, 'blog/mainpage.html', {'posts': posts})

class mainPage(ListView):
    model = Article
    template_name = 'blog/mainpage.html'
    context_object_name = 'posts'
    ordering = ['-time_create']
    paginate_by = 4

class Search(ListView):
    model = Article
    template_name = 'blog/mainpage.html'
    context_object_name = 'posts'
    ordering = ['-time_create']
    paginate_by = 4

    def get_queryset(self):
        if self.request.GET.get('q') is None:
            return Article.objects.all()[::-1]
        return Article.objects.filter(title__iregex=self.request.GET.get('q'))[::-1]

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'blog/register.html'
    success_url = reverse_lazy('about')

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'blog/login.html'
    def get_success_url(self):
        return reverse_lazy('home')

def AboutPage(request):
    return render(request, 'blog/aboutpage.html')

def ShowPost(request, post_id):
    post = Article.objects.get(pk=post_id)
    coms = post.comments_article.all()[::-1]

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            user = User.objects.get(pk=request.user.id)

            comment = form.cleaned_data['content']  # Получение значения поля "comment"
            Comments.objects.create(content=comment, user=user, article=post, username=request.user.username)
            return redirect(request.META.get('HTTP_REFERER'))

    else:
        form = CommentForm()

    return render(request, 'blog/post.html', {'post': post, 'form': form, 'comments': coms})

def logoutUser(request):
    logout(request)
    return redirect('home')
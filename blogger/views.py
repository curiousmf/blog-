from django.shortcuts import render, redirect, get_object_or_404
from blogger.models import Post
from blogger.forms import PostModelForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import CreateView, TemplateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


def start_page(request):
    context = {'blogs': Post.objects.all()}
    if request.method == 'POST':
        blog_id = request.POST.get('like')
        blog = Post.objects.get(pk=blog_id)
        blog.likes += 1
        blog.save()
    return render(request, 'index.html', context=context)




from django.contrib.auth.decorators import login_required

@login_required(login_url='start')
def add_blog(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST)

        if form.is_valid():
            user = request.user
            post = form.save(commit=False)
            post.author = user
            post.save()
        
            return redirect('start')
    
    else:
        form = PostModelForm()

    context = {'form': form}
    return render(request, 'add_blog.html', context=context)

# @login_required(login_url='start')
class EditBlogView(UpdateView):
    model = Post
    slug_field = 'slug'
    template_name = 'edit.html'
    slug_url_kwarg = 'slug'
    form_class = PostModelForm
    success_url = reverse_lazy('start')


def blog(request, blog_id):
    blog = get_object_or_404(Post, id=blog_id)
    return render(request, 'blog.html', context={'blog': blog})


class RegisterViewPage(CreateView):
    template_name = 'registration.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('start')

class LoginPageView(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    next_page = reverse_lazy('start')


class LogoutPageView(LogoutView):
    next_page = reverse_lazy('start')


class DeleteBlogView(DeleteView):
    model = Post
    template_name = 'delete.html'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('start')




def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('start') 
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'change.html', {'form': form})

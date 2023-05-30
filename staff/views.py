
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .forms import *
from .utils import *
from .models import *


class StaffHome(DataMixin, ListView):
    model = Staff
    template_name = 'staff/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Home")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Staff.objects.filter(is_published=True)
    

class UpdatePostView(DataMixin, UpdateView):
    model = Staff
    template_name = 'staff/update_post.html'
    slug_url_kwarg = 'post_slug'
    success_url = reverse_lazy('home')
    fields = ['title', 'content', 'brand', 'size', 'price', 'photo', 'is_published']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="UPDATE")
        return dict(list(context.items()) + list(c_def.items()))
    

class DeletePostView(DataMixin, DeleteView):
    model = Staff
    template_name = 'staff/delete_post.html'
    slug_url_kwarg = 'post_slug'
    success_url = reverse_lazy('home')
 

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="UPDATE")
        return dict(list(context.items()) + list(c_def.items()))


class StaffContact(DataMixin, ListView):
    model = Staff
    template_name = 'staff/feedback.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="FEDDBACK")
        return dict(list(context.items()) + list(c_def.items()))

class ShowPost(DataMixin, DetailView):
    model = Staff
    template_name = 'staff/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


class MyPostsListView(LoginRequiredMixin, DataMixin, ListView):
    model = Staff
    template_name = 'staff/my_posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        return Staff.objects.filter(user=user)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['posts'])
        return dict(list(context.items()) + list(c_def.items()))


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'staff/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="ADD POST")
        return dict(list(context.items()) + list(c_def.items()))

@login_required
def pic_upload(request,user_id):
    user = Staff.objects.get(user__id=user_id)
    for afile in request.FILES.getlist('files'):
        pic = AdditionalImage()
        pic.user= user 
        pic.image = afile
        pic.save()

    return redirect("post")


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'staff/register.html'
    success_url = reverse_lazy('LOGIN')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="REGISTERATE")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'staff/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="LOGIN")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')
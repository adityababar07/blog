from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
# Create your views here.
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404

# from .forms import CommentForm

from .models import Blog, Comment


class HomePageView(TemplateView):
    model = Blog
    template_name = 'home.html'


class BlogListView(LoginRequiredMixin, ListView):
    model = Blog
    template_name = 'blog_list.html'
    login_url = 'login'
    paginate_by = 10  # Enables pagination, displaying 10 blogs per 

class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Blog
    template_name = 'blog_detail.html'
    login_url = 'login'


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'blog_new.html'
    fields = ['title', 'body']
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Blog
    template_name = 'blog_edit.html'
    fields = ['title', 'body']
    success_url = reverse_lazy('blog_list')
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Blog    
    template_name = 'blog_delete.html'
    success_url = reverse_lazy('home')
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class AboutTemplateView(TemplateView):
    template_name = 'about.html'


class BlogCommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'comments/comment_new.html'
    fields = ['comment']
    success_url = reverse_lazy('Blog_list')
    login_url = 'login'
    
    def form_valid(self, form, **kwargs):
        form.instance.author = self.request.user
        # form.instance.todo_id = self.kwargs['pk']
        return super().form_valid(form)
        # return render(request, 'comments/comment_new.html', context)


from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
# Create your views here.
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404
from .forms import CommentForm
from django.core.paginator import Paginator
from accounts.models import CustomUser


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

class BlogDetailView(LoginRequiredMixin,CreateView, DetailView):
    model = Blog
    template_name = 'blog_detail.html'
    form_class = CommentForm
    login_url = 'login'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog = self.get_object()
        comments = blog.comments.all()
        paginator = Paginator(comments, 500)  # Show 5 comments per page
        page_number = self.request.GET.get('page', 1)
        context['comments'] = paginator.get_page(page_number)
        if 'form' not in context:
            context['form'] = self.get_form()
        return context

    def form_valid(self, form):
        blog = self.get_object()  # Get the blog instance
        form.instance.blog = blog 
        form.instance.author = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
        """Redirect to the same blog detail page after submitting a comment."""
        return reverse('blog_detail', kwargs={'pk': self.get_object().pk})

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


class UserSearchView(ListView):
    model = CustomUser
    template_name = 'search_results.html'
    context_object_name = 'users'

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        if query:
            return CustomUser.objects.filter(
                Q(username__icontains=query) | Q(email__icontains=query)
            )
        return CustomUser.objects.none()

# Blog Search View
class BlogSearchView(ListView):
    model = Blog
    template_name = 'search_results.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        if query:
            return Blog.objects.filter(
                Q(title__icontains=query) | Q(body__icontains=query)
            )
        return Blog.objects.none()

# Combined Search View
class SearchResultsView(TemplateView):
    template_name = 'search_results.html'

    def get_context_data(self, **kwargs):
        # Retrieve the default context
        context = super().get_context_data(**kwargs)
        
        # Fetch the search query from the GET parameters
        query = self.request.GET.get('q', '').strip()
        
        if query:
            # Filter users and blogs based on the query
            context['users'] = CustomUser.objects.filter(
                Q(username__icontains=query) | Q(email__icontains=query)
            )
            context['blogs'] = Blog.objects.filter(
                Q(title__icontains=query) | Q(body__icontains=query)
            )
        else:
            # Provide empty QuerySets when no search query is present
            context['users'] = CustomUser.objects.none()
            context['blogs'] = Blog.objects.none()
        
        return context
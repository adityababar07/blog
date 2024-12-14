from django.urls import path

from .views import (HomePageView,
                    BlogListView,
                    BlogDetailView,
                    BlogCreateView,
                    BlogUpdateView,
                    BlogDeleteView,
                    AboutTemplateView,
                    BlogCommentCreateView,
                    UserSearchView,
                    BlogSearchView,
                    SearchResultsView,)

urlpatterns = [
    path('search/users/', UserSearchView.as_view(), name='user_search'),
    
    # For Blog search only
    path('search/blogs/', BlogSearchView.as_view(), name='blog_search'),
    
    # Combined search for both Users and Blogs
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('about/', AboutTemplateView.as_view(), name='about'),
    # path('blog/<int:pk>/comment/', BlogCommentCreateView.as_view(), name='comment_new'),
    path('blog/delete/<int:pk>', BlogDeleteView.as_view(), name='blog_delete'),
    path('blog/edit/<int:pk>', BlogUpdateView.as_view(), name='blog_edit'),
    path('blog/new', BlogCreateView.as_view(), name='blog_new'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('home/', HomePageView.as_view(), name='home'),
    path('', BlogListView.as_view(), name='blog_list'),

]
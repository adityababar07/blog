from django.urls import path

from .views import (
    AboutTemplateView,
    BlogCommentCreateView,
    BlogCreateView,
    BlogDeleteView,
    BlogDetailView,
    BlogListView,
    BlogUpdateView,
    HomePageView,
)

urlpatterns = [
    path("about/", AboutTemplateView.as_view(), name="about"),
    # path('blog/<int:pk>/comment/', BlogCommentCreateView.as_view(), name='comment_new'),
    path("blog/delete/<int:pk>", BlogDeleteView.as_view(), name="blog_delete"),
    path("blog/edit/<int:pk>", BlogUpdateView.as_view(), name="blog_edit"),
    path("blog/new", BlogCreateView.as_view(), name="blog_new"),
    path("blog/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path("blog/", BlogListView.as_view(), name="blog_list"),
    path("", HomePageView.as_view(), name="home"),
]

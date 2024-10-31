from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogListView, BlogCreateView, BlogUpdateView, BlogDetailView, BlogDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('blog_list', BlogListView.as_view(), name='blog_list'),
    path('blog_form/', BlogCreateView.as_view(), name='blog_create'),
    path('blog_form/<int:pk>/update/', BlogUpdateView.as_view(), name='blog_update'),
    path('blog_detail/<int:pk>/detail/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog_delete/<int:pk>/delete/', BlogDeleteView.as_view(), name='blog_delete')
]
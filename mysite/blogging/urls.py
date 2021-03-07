from blogging.views import post_view, list_view
from blogging.views import detail_view
from django.urls import path
from blogging.views import stub_view


urlpatterns = [
    path('', list_view, name="blog_index"),
    path('posts/', post_view, name="post_detail"),
    path('posts/<int:post_id>/', detail_view, name="blog_detail"),
    
]
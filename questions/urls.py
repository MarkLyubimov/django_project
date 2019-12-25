from django.urls import path, re_path, include
from django.conf.urls import url
from django.views.generic import ListView, DetailView
from questions.models import Articles
from .views import ArticleListView, CommentListView, ArticleDetailView, post_new, add_comment_to_post, post_remove


urlpatterns = [
                path('', ArticleListView.as_view(), name='articles_top'),
                path('<int:pk>/', ArticleDetailView.as_view(), name='article_details'),
                path('new/', post_new, name='post_new'),
                path('<int:pk>/comment/', add_comment_to_post, name='add_comment_to_post'),
                path('/<int:pk>/remove/', post_remove, name='post_remove'),
]
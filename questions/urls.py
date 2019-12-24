from django.urls import path, re_path, include
from django.conf.urls import url
from django.views.generic import ListView, DetailView
from questions.models import Articles
from .views import ArticleListView, CommentListView, ArticleDetailView, post_new


urlpatterns = [

    path('', ArticleListView.as_view(), name='articles_top'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_details'),
    path('new/', post_new, name='post_new'),


    # re_path(r'^(?P<pk>\d+)$', ArticleDetailView.as_view(), name='article_details'),
    # path('<int:pk>/', post_detail, name='article_by_index'),
    # path('', ArticleListView.as_view()),
    # re_path(r'^(?P<pk>\d+)$', DetailView.as_view(model=Articles, template_name="questions/post.html")),

]

#
# urlpatterns = [
#     url(r'^blogs/$', BlogListView.as_view(), name="blog-list"),
#     url(r'^blogs/(?P<pk>[0-9]+)/$', BlogDetailView.as_view(), name='blog-details'),
#     url(r'^posts/(?P<pk>[0-9]+)/$', PostDetailView.as_view(), name='post-details'),
# ]

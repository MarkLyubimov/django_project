from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from .forms import PostForm, CommentForm
from django.utils import timezone
from .models import Articles, Comments
from django.contrib.auth.decorators import login_required


# Create your views here.
class ArticleListView(ListView):
    model = Articles
    template_name = "questions/posts.html"
    context_object_name = 'article'


class ArticleDetailView(DetailView):
    model = Articles
    template_name = "questions/post.html"
    context_object_name = 'article'


class CommentListView(ListView):
    model = Comments
    # template_name =
    # context_object_name =


class CommentDetailView(DetailView):
    model = Comments
    # template_name =
    # context_object_name =


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.date = timezone.now()
            post.save()
            return redirect('article_details', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'questions/post_edit.html', {'form': form})


@login_required
def add_comment_to_post(request, pk):
    article = get_object_or_404(Articles, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.postassigned = article
            comment.author = request.user
            comment.save()
            return redirect('article_details', pk=article.pk)
    else:
        form = CommentForm()
    return render(request, 'questions/add_comment_to_post.html', {'form': form})


@login_required
def post_remove(request, pk):
    post = get_object_or_404(Articles, pk=pk)
    post.delete()
    return redirect('articles_top')

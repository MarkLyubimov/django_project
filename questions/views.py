from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from .forms import PostForm
from django.utils import timezone
from .models import Articles, Comments


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





def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.date = timezone.now()
            post.save()
            # return redirect('articles_top', pk=post.pk)
            return redirect('article_details', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'questions/post_edit.html', {'form': form})


# def post_new(request):
#     form = PostForm()
#     return render(request, 'questions/post_edit.html', {'form': form})
# def post_detail(request, pk):
#     q = get_object_or_404(Articles, pk=pk)
#     return render(request, 'questions/post_detail.html', {'q': q})
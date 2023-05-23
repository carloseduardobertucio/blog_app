from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import CommentForm, PostForm

def post_list(request):
    template_name = 'blog/post_list.html'
    posts = Post.objects.all().order_by('-created_at') 

    return render(request, template_name, {'posts': posts})

def post_detail(request, post_id):
    template_name = 'blog/post_detail.html'
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comments.filter(active=True)
    
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog')  # Redirecione para a página desejada após salvar o post
    else:
        form = PostForm()

    return render(request, 'blog/create_post.html', {'form': form})


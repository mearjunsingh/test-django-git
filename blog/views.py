from django.shortcuts import redirect, render

from .forms import SearchForm
from .models import Post


def blog_index_page(request):
    posts = Post.objects.filter(is_published=True).order_by("-views")

    form = SearchForm(request.GET or None)
    if form.is_valid():
        query = form.cleaned_data.get("query")
        posts = posts.filter(title__icontains=query)

    ctx = {"posts": posts}
    return render(request, "blog-index.html", ctx)


def single(request, slug):
    post = Post.objects.get(slug=slug)
    post.views += 1
    post.save()
    print(post.category.title)
    ctx = {"post": post}
    return render(request, "blog-single.html", ctx)


def create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        # Post.objects.create(title=title)
        ob = Post()
        ob.title = title
        ob.save()
        return redirect("blog_index_page")
    return render(request, "blog-create.html")

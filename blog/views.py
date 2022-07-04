from django.shortcuts import redirect, render

from .models import Post


def blog_index_page(request):
    posts = Post.objects.filter(is_published=True).order_by("-views")
    ctx = {"posts": posts}
    return render(request, "blog-index.html", ctx)


def single(request, id):
    post = Post.objects.get(id=id)
    post.views += 1
    post.save()
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

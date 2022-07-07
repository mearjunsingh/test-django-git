from .forms import SearchForm
from .models import Category


def search_form(request):
    form = SearchForm(request.GET or None)
    return {"search_form": form}


def nav_cat(request):
    cats = Category.objects.all()
    return {"nav_cats": cats}

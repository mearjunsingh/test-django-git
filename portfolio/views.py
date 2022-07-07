from django.shortcuts import render

from .forms import ContactForm


def home_page(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():
        print(form.cleaned_data.get("name"))
        form.save()

    ctx = {
        "contact_form": form,
    }
    return render(request, "home-page.html", ctx)

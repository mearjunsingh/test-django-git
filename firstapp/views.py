from django.shortcuts import render


def hello(request):

    try:
        a = int(request.GET.get("num1"))
        b = int(request.GET.get("num2"))

        c = a + b
    except:
        c = "error"

    return render(request, "home.html", {"sum": c})

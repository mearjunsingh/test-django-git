from django.shortcuts import render


def index(request):

    return render(request, "index.html")


def add(request):

    try:
        a = int(request.GET.get("num1"))
        b = int(request.GET.get("num2"))

        c = a + b
    except:
        c = "error"

    ctx = {
        "ans": c,
        "btn_text": "Add",
    }
    return render(request, "calc.html", ctx)


def sub(request):

    try:
        a = int(request.GET.get("num1"))
        b = int(request.GET.get("num2"))

        c = a - b
    except:
        c = "error"
    ctx = {
        "ans": c,
        "btn_text": "Sub",
    }
    return render(request, "calc.html", ctx)


def mul(request):

    try:
        a = int(request.GET.get("num1"))
        b = int(request.GET.get("num2"))

        c = a * b
    except:
        c = "error"

    ctx = {
        "ans": c,
        "btn_text": "Mul",
        "count": 458,
    }
    return render(request, "calc.html", ctx)


def div(request):

    try:
        a = int(request.GET.get("num1"))
        b = int(request.GET.get("num2"))

        c = a / b
    except:
        c = "error"

    ctx = {
        "ans": c,
        "btn_text": "Div",
    }
    return render(request, "calc.html", ctx)

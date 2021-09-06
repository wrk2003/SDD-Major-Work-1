from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from . import file_handling

# Create your views here.

def index(request):
    return render(request, "index.html")

def staircase(request):
    if request.method == "POST":
        form = forms.Code(request.POST)
        if form.is_valid():
            file_handling.CreatePythonFile("hello", form.clean_code())
            pass_fail = file_handling.ExecutePythonFile("hello", ["1 2", "2 3"])

    else:
        form = forms.Code(initial={"code": ""})
        pass_fail = []

    context = {
        "form": form,
        "pass_fail": pass_fail
    }

    return render(request, "problems/staircase.html", context=context)

def sam(request):
    return render(request, "problems/sam-and-substrings.html")

def morgan(request):
    return render(request, "problems/morgan-and-a-string.html")

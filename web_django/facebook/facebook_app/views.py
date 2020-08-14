from django.shortcuts import render
from django.http import HttpResponse
from .models import ShoeModelForm


# Create your views here.
def home_view(request, *args, **kwargs):
    return HttpResponse("<h1>helllooo</h1>")

def new_view(request, *args, **kwargs):
    my_context = {
    "sion": 21,
    "alex": 23,
    "family": [21, 22, 23, 24]
    }
    return render(request, 'webuygold copy.html', my_context )

def model_view(request, *args, **kwargs):
    form = ShoeModelForm()
    if request.method == "POST":
        form = ShoeModelForm(request.POST)
        if form.is_valid():
            form.save()
            return home_view(request)
    return render(request, 'modelform.html', {'form' : form})

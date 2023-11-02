from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    if request.method == "POST":
        entery_name = request.POST.get("name")
        entery_last_name = request.POST.get("lastName")
        SignIn.objects.create(name = entery_name , lastName = entery_last_name)
    return render(request,"ajax_app/index.html")
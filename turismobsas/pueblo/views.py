from django.shortcuts import render
from .models import Project
# Create your views here.
def pueblo(request):
    projects = Project.objects.all()
    return render(request, "pueblo/pueblo.html", {'projects':projects})


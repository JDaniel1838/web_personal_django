from django.shortcuts import render
from .models import Project

# Create your views here.
#view portfolio
def portfolio(request):
    projects = Project.objects.all()
    return render(request,'portfolio/portfolio.html',{'title': "Portafolio | Mi Web Personal",'projects':projects})

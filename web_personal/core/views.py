from django.shortcuts import render
from django.shortcuts import render, HttpResponse

# view home
def home(request):
    return render(request,'core/home.html')

# view about
def about(request):
    return render(request,'core/about.html')

# view portfolio
def portfolio(request):
    return render(request,'core/portfolio.html')

# view contact
def contact(request):
    return render(request,'core/contact.html')

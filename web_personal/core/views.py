from django.shortcuts import render
# view home
def home(request):
    return render(request,'core/home.html',{'title': "Portada | Mi Web Personal"})

# view about
def about(request):
    return render(request,'core/about.html',{'title': "Acerca de | Mi Web Personal"})

# view contact
def contact(request):
    return render(request,'core/contact.html',{'title': "Contacto | Mi Web Personal"})

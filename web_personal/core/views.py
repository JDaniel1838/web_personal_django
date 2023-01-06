from django.shortcuts import render
from django.shortcuts import render, HttpResponse

# var menu with code HTML.
html_base = """
 <h1>Mi Web Personal</h1>
 <ul>
 <li><a href="/">Portada</a></li>
 <li><a href="/about/">Acerca de</a></li>
 <li><a href="/portfolio/">Portafolio</a></li>
 <li><a href="/contact/">Contacto</a></li>
 </ul>
"""

# view home
def home(request):
    return HttpResponse(html_base + """
        <h2>Bienvenidos</h2>
        <p>Esto es la portada.</p>
    """)

# view about
def about(request):
    return HttpResponse("""
    <h1>Mi Web Personal</h1>
    <h2>Acerca de</h2>
    <p>Me llamo Daniel y me encanta Django!</p>
    """)

# view portfolio
def portfolio(request):
    return HttpResponse("""
    <h2>Mi portafolio</h2>
    <p>Aquí encontraras todos mis proyectos</p>
    """)

# view contact
def contact(request):
    return HttpResponse("""
    <h2>Contacto</h2>
    <p>Aquí encontraras mi email y redes sociales para contactarme</p>
    <ul>
        <li><a href='www.google.com'>Email</a></li>
        <li><a href='www.github.com'>Github</a></li>
        <li><a href='www.youtube.com'>Youtube</a></li>
    </ul>
    """)

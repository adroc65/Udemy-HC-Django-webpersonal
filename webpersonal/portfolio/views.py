from django.shortcuts import render
from .models import Project


# Create your views here.
def portfolio(request):
    # Se procede a leer todos los OBJETOS que tiene el modelo de Proyecto
    projects = Project.objects.all()
    # Se inyecta la lista de proyectos a la vista
    return render(request, "portfolio/portfolio.html", {'projects': projects})

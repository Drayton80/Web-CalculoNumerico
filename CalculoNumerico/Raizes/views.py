from django.shortcuts import render

# Create your views here.
def paginaInicial(request):
	contexto = {}
	return render(request, "Raizes/base.html", contexto)
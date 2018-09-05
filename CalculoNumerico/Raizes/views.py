from django.shortcuts import render
from numpy import *
from .algorithms1 import numeric_methods
import numpy as np
import math
import matplotlib.pyplot as plt, mpld3


# Create your views here.

contexto = {}
def paginaInicial(request):
	if request.method == "POST" and 'falsaPosicaoSalvar' in request.POST:
		print(request.POST)
		equacao = numeric_methods.replace_Exponentiation(str(request.POST.get('falsaPosicaoEquacaoInput')))
		LI = str(eval(numeric_methods.replace_Exponentiation(str(request.POST.get("falsaPosicaoLIInput")))))
		LU = str(eval(numeric_methods.replace_Exponentiation(str(request.POST.get("falsaPosicaoLSInput")))))
		tol = str(eval(numeric_methods.replace_Exponentiation(str(request.POST.get("falsaPosicaoToleranciaInput")))))
		erro = str(request.POST.get("falsaPosicaoErro"))
		print(
			'equacao:' , equacao, '\n',
			'Limite Inferior:' , LI, '\n',
			'Limte Superior:' , LU, '\n',
			'tolerancia:' , tol, '\n'
			"Erro:", erro, '\n'
			)
		contexto['graph'] = grafico()
		pass

	elif request.method == "POST" and 'secanteSalvar' in request.POST:
		print(request.POST)
		equacao = numeric_methods.replace_Exponentiation(str(request.POST.get('secanteEquacaoInput')))
		x0 = str(eval(numeric_methods.replace_Exponentiation(str(request.POST.get("secanteX0Input")))))
		x1 = str(eval(numeric_methods.replace_Exponentiation(str(request.POST.get("secanteX1Input")))))
		tol = str(eval(numeric_methods.replace_Exponentiation(str(request.POST.get("falsaPosicaoToleranciaInput")))))
		erro = request.POST.get("secateErro")
		print(
			'equacao:' , equacao, '\n',
			'x0:' , x0, '\n',
			'x1:' , x1, '\n',
			'tolerancia:' , tol, '\n',
			'Erro', erro, '\n',
			)
		pass

	elif request.method == "POST" and 'mullerSalvar' in request.POST:
		equacao = numeric_methods.replace_Exponentiation(str(request.POST.get('mullerEquacaoInput')))
		x0 = str(eval(numeric_methods.replace_Exponentiation(str(request.POST.get("mullerX0Input")))))
		x1 = str(eval(numeric_methods.replace_Exponentiation(str(request.POST.get("mullerX1Input")))))
		x2 = str(eval(numeric_methods.replace_Exponentiation(str(request.POST.get("mullerX2Input")))))
		tol = str(eval(numeric_methods.replace_Exponentiation(str(request.POST.get("mullerToleranciaInput")))))
		erro = request.POST.get("mullerErro")
		print(
			'equacao:' , equacao, '\n',
			'x0:' , x0, '\n',
			'x1:' , x1, '\n',
			'x2:' , x2, '\n',
			'tolerancia:' , tol, '\n',
			'Erro', erro, '\n',
			)
		result, itera = numeric_methods.muller(equacao,x0,x1,x2,tol)
		contexto['resultadoMuller'] = result
		contexto['iteracoesMuller'] = itera
		pass

	return render(request, "Raizes/base.html", contexto)



def grafico():
	t = linspace(0,2*math.pi,400)
	a = sin(t)
	b = cos(t)
	c = a + b
	fig = plt.figure()
	plt.style.use('ggplot')
	plt.plot(t, a, t, b, t, c)
	#mpld3.enable_notebook()
	html_graph = mpld3.fig_to_html(fig)
	return html_graph

from django.shortcuts import render
from numpy import *
import numpy as np
import math
import matplotlib.pyplot as plt, mpld3

# Create your views here.
def paginaInicial(request):
	if request.method == "POST" and 'falsaPosicaoSalvar' in request.POST:
		print(request.POST)
		equacao = request.POST.get('falsaPosicaoEquacaoInput')
		LI = request.POST.get("falsaPosicaoLIInput")
		LU = request.POST.get("falsaPosicaoLSInput")
		tolerancia = request.POST.get("falsaPosicaoToleranciaInput")
		erro = request.POST.get("falsaPosicaoErro")
		print(
			'equacao:' , equacao, '\n',
			'Limite Inferior:' , LI, '\n',
			'Limte Superior:' , LU, '\n',
			'tolerancia:' , tolerancia, '\n'
			"Erro:", erro, '\n'
			)
		pass

	elif request.method == "POST" and 'secanteSalvar' in request.POST:
		print(request.POST)
		equacao = request.POST.get('secanteEquacaoInput')
		x0 = request.POST.get("secanteX0Input")
		x1 = request.POST.get("secanteX1Input")
		tolerancia = request.POST.get("falsaPosicaoToleranciaInput")
		erro = request.POST.get("secateErro")
		print(
			'equacao:' , equacao, '\n',
			'x0:' , x0, '\n',
			'x1:' , x1, '\n',
			'tolerancia:' , tolerancia, '\n',
			'Erro', erro, '\n',
			)
		pass

	elif request.method == "POST" and 'mullerSalvar' in request.POST:
		equacao = request.POST.get('mullerEquacaoInput')
		x0 = request.POST.get("mullerX0Input")
		x1 = request.POST.get("mullerX1Input")
		x2 = request.POST.get("mullerX2Input")
		tolerancia = request.POST.get("mullerToleranciaInput")
		erro = request.POST.get("mullerErro")
		print(
			'equacao:' , equacao, '\n',
			'x0:' , x0, '\n',
			'x1:' , x1, '\n',
			'x2:' , x2, '\n',
			'tolerancia:' , tolerancia, '\n',
			'Erro', erro, '\n',
			)
		pass

	contexto = {'graph': grafico()}
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

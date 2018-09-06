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
		result, itera = numeric_methods.falsaPosicao(equacao,LI,LU,tol,1000, erro)

		contexto['resultadoFalsaPosicao'] = result
		contexto['iteracoesFalsaPosicao'] = itera
		contexto['graphFalsaPosicao'] = numeric_methods.plota_func(equacao)
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
		result, itera = numeric_methods.muller(equacao,x0,x1,x2,tol,erro)
		contexto['resultadoMuller'] = result
		contexto['iteracoesMuller'] = itera
		contexto['graphMuller'] = numeric_methods.plota_func(equacao)

		pass

	return render(request, "Raizes/base.html", contexto)
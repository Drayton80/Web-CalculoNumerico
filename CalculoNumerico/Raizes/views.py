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
		xmin = float(request.POST.get("falsaPosicaoGraficoMenorX"))
		xmax = float(request.POST.get("falsaPosicaoGraficoMaiorX"))
		print(
			'equacao:' , equacao, '\n',
			'Limite Inferior:' , LI, '\n',
			'Limte Superior:' , LU, '\n',
			'tolerancia:' , tol, '\n',
			"Erro:", erro, '\n',
			"xmin:", xmin, '\n',
			"xmax:", xmax, '\n'
			)
		result, itera = numeric_methods.falsaPosicao(equacao,LI,LU,tol,1000, erro)

		contexto['resultadoFalsaPosicao'] = result
		contexto['iteracoesFalsaPosicao'] = itera
		contexto['graphFalsaPosicao'] = numeric_methods.plota_func(equacao, xmin, xmax)
		pass

	elif request.method == "POST" and 'secanteSalvar' in request.POST:
		print(request.POST)
		equacao = numeric_methods.replace_Exponentiation(str(request.POST.get('secanteEquacaoInput')))
		x0 = str(eval(numeric_methods.replace_Exponentiation(str(request.POST.get("secanteX0Input")))))
		x1 = str(eval(numeric_methods.replace_Exponentiation(str(request.POST.get("secanteX1Input")))))
		tol = str(eval(numeric_methods.replace_Exponentiation(str(request.POST.get("secanteToleranciaInput")))))
		erro = request.POST.get("secateErro")
		xmin = float(request.POST.get("secanteGraficoMenorX"))
		xmax = float(request.POST.get("secanteGraficoMaiorX"))
		print(
			'equacao:' , equacao, '\n',
			'x0:' , x0, '\n',
			'x1:' , x1, '\n',
			'tolerancia:' , tol, '\n',
			'Erro', erro, '\n',
			"xmin:", xmin, '\n',
			"xmax:", xmax, '\n'
			)

		result, itera = numeric_methods.secante(equacao,x0,x1,tol,1000,erro)
		contexto['resultadoSecante'] = result
		contexto['iteracoesSecante'] = itera
		contexto['graphSecante'] = numeric_methods.plota_func(equacao, xmin, xmax)
		pass

	elif request.method == "POST" and 'mullerSalvar' in request.POST:
		equacao = numeric_methods.replace_Exponentiation(str(request.POST.get('mullerEquacaoInput')))
		x0 = str(eval(numeric_methods.replace_Exponentiation(str(request.POST.get("mullerX0Input")))))
		x1 = str(eval(numeric_methods.replace_Exponentiation(str(request.POST.get("mullerX1Input")))))
		x2 = str(eval(numeric_methods.replace_Exponentiation(str(request.POST.get("mullerX2Input")))))
		tol = str(eval(numeric_methods.replace_Exponentiation(str(request.POST.get("mullerToleranciaInput")))))
		erro = request.POST.get("mullerErro")
		xmin = float(request.POST.get("mullerGraficoMenorX"))
		xmax = float(request.POST.get("mullerGraficoMaiorX"))
		print(
			'equacao:' , equacao, '\n',
			'x0:' , x0, '\n',
			'x1:' , x1, '\n',
			'x2:' , x2, '\n',
			'tolerancia:' , tol, '\n',
			'Erro', erro, '\n',
			"xmin:", xmin, '\n',
			"xmax:", xmax, '\n'
			)
		result, itera = numeric_methods.muller(equacao,x0,x1,x2,tol,erro)
		contexto['resultadoMuller'] = result
		contexto['iteracoesMuller'] = itera
		contexto['graphMuller'] = numeric_methods.plota_func(equacao, xmin, xmax)

		pass

	return render(request, "Raizes/base.html", contexto)



def miniProjeto2(request):
	contexto['tagteste'] = "<div class=\"form-group col-lg-6\"> <input type=\"text\" class=\"form-control\" id=\"gaussJordanTamanhoInput\" placeholder=\"Coloque valores inteiros entre 2 e 5\" name = \"gaussJordanTamanhoInput\"> </div>"
	if request.method == "POST" and 'tamanhoSistema' in request.POST:
		contexto['tamanhoSistema'] = range(int(request.POST.get('gaussJordanTamanhoInput')))
	
	#if request.method == "POST" and 'sistemasLineares' in request.POST:
	return render(request, "Raizes/base2.html", contexto)



from django.shortcuts import render
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


def tagMatriz(tamanho, metodo):
	#Criação da matriz
	tag = ''
	for i in range(1, tamanho + 1):
		#Começo da linha
		tag += '<div class=\"d-flex justify-content-center\">'
		if(metodo == "gaussJordan"):
			for j in range(1, tamanho + 2):
				if(j != tamanho + 1):
					#Imput
					#Basico da criação do imput
					tag += '<input type=\"text\" class=\"form-control\"'
					tag += 'placeholder=\"a' +  str(i) + str(j) + "\""
					tag += 'id=\"' + metodo + 'a' + str(i) + str(j) + '\"'
					tag += 'name = \"' + metodo + 'a' + str(i) + str(j) + '\">'
				else:
					tag += '<input type=\"text\" class=\"form-control ml-4\"'
					tag += 'placeholder=\"b' +  str(i) + "\""
					tag += 'id=\"' + metodo + 'b' + str(i) + '\"'
					tag += 'name = \"' + metodo + 'b' + str(i) + '\">'

		elif metodo == "NewtonNaoLinear":
			tag += '<input type=\"text\" class=\"form-control\"'
			tag += 'placeholder=\"f(x' +  str(i) + ")\""
			tag += 'id=\"' + metodo + 'fx' + str(i) + '\"'
			tag += 'name = \"' + metodo + 'fx' + str(i) + '\">'

			tag += '<input type=\"text\" class=\"form-control ml-2\"'
			tag += 'placeholder=\"Valor inicial x' + str(i) + '\"'
			tag += 'id=\"' + metodo + 'x' + str(i) + '\"'
			tag += 'name = \"' + metodo + 'x' + str(i) + '\">'

		elif metodo == "splinesCubico":
			tag += '<input type=\"text\" class=\"form-control\"'
			tag += 'placeholder=\"ponto x' +  str(i) + "\""
			tag += 'id=\"' + metodo + 'x' + str(i) + '\"'
			tag += 'name = \"' + metodo + 'x' + str(i) + '\">'

			tag += '<input type=\"text\" class=\"form-control ml-2\"'
			tag += 'placeholder=\"ponto y' + str(i) + '\"'
			tag += 'id=\"' + metodo + 'y' + str(i) + '\"'
			tag += 'name = \"' + metodo + 'y' + str(i) + '\">'

		#Fim da linha
		tag += '</div>'
	return tag

def tagVetorResposta(valores):
	tag = '<div class=\"d-flex flex-column align-items-center\">'
	for valor in valores:
		tag += '<input class="form-control\" type=\"text\"'
		tag += 'placeholder = \"' + str(valor) + '\" readonly>'

	tag += '</div>'
	return tag

def backTagGeradas(tamanho, metodo, request):
	if metodo == "gaussJordan":		
		matriz = []
		resultado = []
		for i in range(1, tamanho + 2):
			print("oooooooooooooooooooiiiiiiiiiiiiiiiI", i)
			linha = []
			resultado.append(int(request.POST.get(metodo + 'b'  + str(i))))
			for j in range(1, tamanho + 2):
				linha.append(int(request.POST.get(metodo + 'a'  + str(i) + str(j))))
			matriz.append(linha)

		return matriz, resultado

	elif metodo == "NewtonNaoLinear":
		funcoes = []
		x0 = []
		for i in range(1, tamanho + 2):
			funcoes.append(str(request.POST.get(metodo + 'fx'  + str(i))))
			x0.append(int(request.POST.get(metodo + 'x'  + str(i))))
		return funcoes, x0

	elif metodo == "splinesCubico":
		x = []
		y = []
		for i in range(1, tamanho + 1):
			x.append(int(request.POST.get(metodo + 'x'  + str(i))))
			y.append(int(request.POST.get(metodo + 'y'  + str(i))))
		return x, y




def miniProjeto2(request):
	print(request.POST)

	#Monta matriz Gauss
	if request.method == "POST" and 'gaussJordanTamanhoInput' in request.POST:
		contexto['ordemGauss'] = int(request.POST.get('gaussJordanTamanhoInput'))
		if contexto['ordemGauss'] != 0:
			contexto['matrizGauss'] = tagMatriz(contexto['ordemGauss'], "gaussJordan")
			contexto['tamanhoGauss'] = True

	#Monta lista de funções de newton
	elif request.method == "POST" and 'newtonTamanhoInput' in request.POST:
		contexto['ordemNewton'] = int(request.POST.get('newtonTamanhoInput'))
		if contexto['ordemNewton'] != 0:
			contexto['matrizNewton'] = tagMatriz(contexto['ordemNewton'], "NewtonNaoLinear")
			contexto['tamanhoNewton'] = True

	#Monta lista de funções de splines
	elif request.method == "POST" and 'splinesTamanhoInput' in request.POST:
		contexto['ordemSplines'] = int(request.POST.get('splinesTamanhoInput'))
		if contexto['ordemSplines'] != 0:
			contexto['matrizSplines'] = tagMatriz(contexto['ordemSplines'], "splinesCubico")
			contexto['tamanhoSplines'] = True


	#Processamento dos valores de Gauss
	elif request.method == "POST" and request.POST.get('valoresJordan') == "True":
		matriz, resultado = backTagGeradas(contexto['ordemGauss'], "gaussJordan", request)
		x = numeric_methods.gaussjordan(matriz, resultado)
		print("MATRIZ-----", matriz, "VETOR RESULTADO-------",resultado, "VALORES DE X:", x, sep = '\n')
		contexto['resultadoGauss'] = tagVetorResposta(x)

	#Processamento dos valores de Newton
	elif request.method == "POST" and request.POST.get('valoresNewton') == "True":
		fx, x0 = backTagGeradas(contexto['ordemSplines'], "NewtonNaoLinear", request)
		tolerancia = numeric_methods.replace_Exponentiation(request.POST.get('newtonToleranciaInput'))
		x = numeric_methods.NewtonNonLinear(fx, x0, tolerancia)
		print("Lista-----", fx, "VETOR chutes-------", x0, "VALORES DE X*:", x, sep = '\n')
		contexto['resultadoNewton'] = tagVetorResposta(x)

	elif request.method == "POST" and request.POST.get('valoresSplines') == "True":
		x, y = backTagGeradas(contexto['ordemSplines'], "splinesCubico", request)
		print("Valores em x-----", x, "Valores em y------", y, sep = '\n')
		funcoes, contexto['graphSplines'] = numeric_methods.splinesCubico(x,y)
		contexto['resultadoSplines'] = tagVetorResposta(funcoes)

	#elif request.method == "POST" and 'gaussJordanTamanhoInput' in request.POST
	return render(request, "Raizes/base2.html", contexto)



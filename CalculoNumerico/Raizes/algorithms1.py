import matplotlib.pyplot as plt, mpld3
import numpy as np
from .Package1.muller import metodo_muller
#from .Package1.secante import secante
from .Package1.falsaP2 import falsaP


class numeric_methods:

	def evalFunction(f,x):
		x=eval(f)
		return x

	def muller(fx, x0, x1, x2, parada, tipoErro):
		return metodo_muller.mullerFunc(fx, x0, x1, x2, parada, tipoErro)

	def falsaPosicao(fx, a, b, tol, maxI, tipoErro):	
		return falsaP.falsaPosicao(fx, a, b, tol, maxI, tipoErro)

	#Aux functions
	def replace_Exponentiation(equation):
		equation = equation.replace("^", "**")
		return equation

	#-----------------Calcula Função------------------#
	def calculaFunc(x, function):
		#function = function.replace('x', 'number')
		return eval(function)#eval calcula o resultado da função desejada
	#--------------Fim Calcula Função-----------------#

	#-----------------Plota Função--------------------#
	def plota_func(function):

		data = list(function)#Cria uma lista para verificar simbolos
		func = function

		for aux in data:
			if aux == '^':
				func = func.replace('^', '**')#Se '^' is True, replace para '**'

		x = np.arange(-100, 100, 0.02)#Limitante de range do gráfico da função

		#print(x)
		#print(func)
		#print(calculaFunc(x, func))
		fig = plt.figure()
		plt.plot(x, numeric_methods.calculaFunc(x, func), 'k')#Plota o gráfico levando em consideração o resultado da função
		plt.axhline(linewidth=0.9, color='black')#Cria a linha do eixo X
		plt.axvline(linewidth=0.9, color='black')#Cria linha do eixo Y
		html_graph = mpld3.fig_to_html(fig)
		return html_graph
		#print(func)
	#--------------Fim Plota Função-------------------#
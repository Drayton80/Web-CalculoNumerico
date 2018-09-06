import numpy as np
import matplotlib.pyplot as plt

#-------------------Funções-----------------------#

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
	plt.plot(x, calculaFunc(x, func), 'k')#Plota o gráfico levando em consideração o resultado da função
	plt.axhline(linewidth=0.9, color='black')#Cria a linha do eixo X
	plt.axvline(linewidth=0.9, color='black')#Cria linha do eixo Y
	plt.show()
	#print(func)
#--------------Fim Plota Função-------------------#

#----------------Fim das Funções------------------#

#func = 'x^2'
func = '-3*x**3 + 2*x**2 + x + 3'
plota_func(func)

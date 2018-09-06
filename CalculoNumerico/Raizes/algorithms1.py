import matplotlib.pyplot as plt, mpld3
import numpy as np

class numeric_methods:

	def evalFunction(f,x):
		x=eval(f)
		return x

	def muller(fx, x0, x1, x2, parada):

		maxiterations = 100
		err = 1000
		i = 0
		print('tipo:', type(x0))
		#convertendo os strings
		x0 = float(x0)
		x1 = float(x1)
		x2 = float(x2)
		parada = float(parada)

		while (i < maxiterations):

			fp0 = numeric_methods.evalFunction(fx, x0)
			fp1 = numeric_methods.evalFunction(fx, x1)
			fp2 = numeric_methods.evalFunction(fx, x2)

			h0 = x1-x0
			h1 = x2-x1
	 

			s0 = (fp1 - fp0)/h0
			s1 = (fp2 - fp1)/h1

			a = (s1-s0)/(h1+h0)
			b = (a * h1) + s1
			c = fp2

			i += 1

			p1 = (-2*c)/(b+((b**2)-4*a*c)**.5)
			p2 = (-2*c)/(b-((b**2)-4*a*c)**.5)

			if b>0:
				p3 = p1+ x2
			if b<0:
				p3 = p2 + x2

			#calculo do erro
			err = abs(p3 - x2)/abs(p3)

			#criterio de parada
			if err <= parada:
				return p3, i
				break
				
			#trocando os valores para os mais atuais
			x0 = x1
			x1 = x2
			x2 = p3

	def falsaPosicao(fx, a, b, tol, maxI, tipoErro):
			
		maxI = int(maxI)
		a = float(a)
		b = float(b)
		tol = float(tol)
		tipoErro = tipoErro
		nIteracoes = 0
		err = 1000

		fa = numeric_methods.evalFunction(fx, a)
		fb = numeric_methods.evalFunction(fx, b)

		if numeric_methods.evalFunction(fx, a) * numeric_methods.evalFunction(fx, b) >= 0:
			raise Exception("A função deve ter sinais opostos para a e b")
		c = a

		while (nIteracoes < maxI):
			aux = c
			fa = numeric_methods.evalFunction(fx, a)
			fb = numeric_methods.evalFunction(fx, b)
			c = ((a * fb) - (b * fa)) / (fb - fa)
			fc = numeric_methods.evalFunction(fx, c)

			nIteracoes += 1

			if tipoErro == 'erroAbsoluto':
				err = (c) - (aux)

			if tipoErro == 'erroRelativo':
				err = ((c) - (aux))/(c)

			if abs(err) < abs(tol):
				return c, nIteracoes
				break

			if fc == 0:
				return c, nIteracoes
				break
							
			elif fc * fa < 0:
				b = c
			else:
				a = c

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
import math

class metodo_muller:
	
	def evalFunction(f,x):
		x=eval(f)
		return x

	def mullerFunc(fx, x0, x1, x2, parada, erro):
		
		maxiterations = 100
		err = 1000
		i = 0
		
		#convertendo os strings
		x0 = float(x0)
		x1 = float(x1)
		x2 = float(x2)
		parada = float(parada)

		while (i < maxiterations):

			fp0 = metodo_muller.evalFunction(fx, x0)
			fp1 = metodo_muller.evalFunction(fx, x1)
			fp2 = metodo_muller.evalFunction(fx, x2)

			h0 = x1-x0
			h1 = x2-x1
	 

			s0 = (fp1 - fp0)/h0
			s1 = (fp2 - fp1)/h1

			a = (s1-s0)/(h1+h0)
			b = (a * h1) + s1
			c = fp2

			i += 1

			if b>0:
				p1 = (-2*c)/(b+math.sqrt((b**2)-4*a*c))
				p3 = p1+ x2
			if b<0:
				p2 = (-2*c)/(b-math.sqrt((b**2)-4*a*c))
				p3 = p2 + x2

			#calculo do erro
			if (erro == 'erroAbsoluto'):
				err = abs(p3 - x2)

			elif (erro == 'erroRelativo'):
				err = abs(p3 - x2)/abs(p3)

			#criterio de parada
			if err <= parada:
				return p3, i
				break
				
			#trocando os valores para os mais atuais
			x0 = x1
			x1 = x2
			x2 = p3


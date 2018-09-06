class metodo_secante:
	def evalFunction(f, x):
		x = eval(f)
		return x


	def secante(f, x0, x1, tolerancia, limiteIteracoes, criterioParada):
		# Os valores chegam como String, então é preciso convertê-los:
		x0 = float(x0)
		x1 = float(x1)
		tolerancia = float(tolerancia) 
		limiteIteracoes = int(limiteIteracoes)

		i = 0

		while i <= limiteIteracoes:
			# Cálculo da f(xk-1):
			fx0 = metodo_secante.evalFunction(f, float(x0))
			# Cálculo da f(xk):
			fx1 = metodo_secante.evalFunction(f, float(x1))

			# Cálculo do Próximo x
			xP = (x0*fx1 - x1*fx0)/(fx1 - fx0)

			# Comparação dos critérios de parada:
			if criterioParada == "erroAbsoluto":
				erro = abs(xP - x1)
			elif criterioParada == "erroRelativo":
				erro = abs(xP - x1)/abs(xP)

			if erro <= tolerancia:
				return xP, i

			# Atualiza o xk-1 e o xk:
			x0 = x1
			x1 = xP

			i += 1


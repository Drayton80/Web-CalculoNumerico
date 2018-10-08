from scipy.optimize import fsolve
import numpy as np

class NewtonNonLinearSystems:
	def __init__(self):
		# Futuras Strings relativas às funções, são globais pois precisam ser referenciadas
		# tanto em f (que estritamente só pode possuir um parâmetro devido ao seu uso no método do scipy)
		# quanto en newton_sistemas_nao_lineares
		self.fx1 = None
		self.fx2 = None
		self.fx3 = None
		self.fx4 = None
		self.fx5 = None
		self.fx6 = None
		self.fx7 = None

	def f(self, fx):
		f = np.zeros(len(fx))

		if(2 == len(fx)):
			x1 = fx[0]
			x2 = fx[1]
		elif(3 == len(fx)):
			x1 = fx[0]
			x2 = fx[1]
			x3 = fx[2]
		elif(4 == len(fx)):
			x1 = fx[0]
			x2 = fx[1]
			x3 = fx[2]
			x4 = fx[3]
		elif(5 == len(fx)):
			x1 = fx[0]
			x2 = fx[1]
			x3 = fx[2]
			x4 = fx[3]
			x5 = fx[4]
		elif(6 == len(fx)):
			x1 = fx[0]
			x2 = fx[1]
			x3 = fx[2]
			x4 = fx[3]
			x5 = fx[4]
			x6 = fx[5]
		elif(7 == len(fx)):
			x1 = fx[0]
			x2 = fx[1]
			x3 = fx[2]
			x4 = fx[3]
			x5 = fx[4]
			x6 = fx[5]
			x7 = fx[6]

		if(2 == len(fx)):
			f[0] = eval(self.fx1)
			f[1] = eval(self.fx2)
		elif(3 == len(fx)):
			f[0] = eval(self.fx1)
			f[1] = eval(self.fx2)
			f[2] = eval(self.fx3)
		elif(4 == len(fx)):
			f[0] = eval(self.fx1)
			f[1] = eval(self.fx2)
			f[2] = eval(self.fx3)
			f[3] = eval(self.fx4)
		elif(5 == len(fx)):
			f[0] = eval(self.fx1)
			f[1] = eval(self.fx2)
			f[2] = eval(self.fx3)
			f[3] = eval(self.fx4)
			f[4] = eval(self.fx5)
		elif(6 == len(fx)):
			f[0] = eval(self.fx1)
			f[1] = eval(self.fx2)
			f[2] = eval(self.fx3)
			f[3] = eval(self.fx4)
			f[4] = eval(self.fx5)
			f[5] = eval(self.fx6)
		elif(7 == len(fx)):
			f[0] = eval(self.fx1)
			f[1] = eval(self.fx2)
			f[2] = eval(self.fx3)
			f[3] = eval(self.fx4)
			f[4] = eval(self.fx5)
			f[5] = eval(self.fx6)
			f[6] = eval(self.fx7)

		return f


	def get_root(self, fx, x0, tolerancia):
		if(len(fx) < 2 or 7 < len(fx)):
			return None

		if(len(fx) == 2):
			self.fx1 = fx[0]
			self.fx2 = fx[1]
		elif(len(fx) == 3):
			self.fx1 = fx[0]
			self.fx2 = fx[1]
			self.fx3 = fx[2]
		elif(len(fx) == 4):
			self.fx1 = fx[0]
			self.fx2 = fx[1]
			self.fx3 = fx[2]
			self.fx4 = fx[3]
		elif(len(fx) == 5):
			self.fx1 = fx[0]
			self.fx2 = fx[1]
			self.fx3 = fx[2]
			self.fx4 = fx[3]
			self.fx5 = fx[4]
		elif(len(fx) == 6):
			self.fx1 = fx[0]
			self.fx2 = fx[1]
			self.fx3 = fx[2]
			self.fx4 = fx[3]
			self.fx5 = fx[4]
			self.fx6 = fx[5]
		elif(len(fx) == 7):
			self.fx1 = fx[0]
			self.fx2 = fx[1]
			self.fx3 = fx[2]
			self.fx4 = fx[3]
			self.fx5 = fx[4]
			self.fx6 = fx[5]
			self.fx7 = fx[6]

		return fsolve(self.f, x0, xtol=tolerancia)

	def set_fx1(self, fx1):
		self.fx1 = fx1

	def set_fx2(self, fx2):
		self.fx2 = fx2

	def set_fx3(self, fx3):
		self.fx3 = fx3

	def set_fx4(self, fx4):
		self.fx4 = fx4

	def set_fx5(self, fx5):
		self.fx5 = fx5

	def set_fx6(self, fx6):
		self.fx6 = fx6

	def set_fx7(self, fx7):
		self.fx7 = fx7

''' Ex. de Uso:
newton = NewtonNonLinearSystems()

fx = ["x1+x2-3","x1**2+x2**2-9"]
x0 = [1,5]
tolerancia = 10**(-5)

fsolved = newton.get_root(fx, x0, tolerancia)

# Print final de x*:
print(fsolved)

# Validação do funcionamento
print(newton.f(fsolved))
'''
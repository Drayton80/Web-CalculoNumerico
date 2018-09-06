''' Metodo da Secante para encontar a raiz de uma funcao
	x= x1-f(x1)*(x1-x0)/(f(x1)-f(x0)). Entrada de dados: xo, x1,
	tolerancia,numero de iteracoes maximas e funcao
'''    
class secante:
	def evalFunction(f, x):
			x = eval(f)
			return x


	def Secante(f,x0,x1,tol,N,tipoErro):
		c = x0
		while i<=N:
			aux = c
			x = fx1 - (fx1-x0)*fx1/(fx1-fx0)  
			
			if tipoErro == 'erroAbsoluto':
				err = (c) - (aux)

			if tipoErro == 'erroRelativo':
				err = ((c) - (aux))/(c)

			print(i,x)
			if abs(err)<tol:
				return i, x
				
			fx0=fx1    # redefinir x0
			fx1=x     #redefinir x1
			i = i + 1

		print('o metodo fracasso depois de %d iteraciones' %N)


import math     
    
    # Exemplo
tipoErro = 'erroAbsoluto'
f='x**3 + 4*x**2 - 10'
x0=1
x1=2
tol=0.0001
N=20
    
x=secante.Secante(f, x0,x1,tol,N,tipoErro)
print()
print('A solcao he: ',x)
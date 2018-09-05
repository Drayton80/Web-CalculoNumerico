
''' Metodo da Secante para encontar a raiz de uma funcao
    x= x1-f(x1)*(x1-x0)/(f(x1)-f(x0)). Entrada de dados: xo, x1,
    tolerancia,numero de iteracoes maximas e funcao
'''    
def Secante(x0,x1,tol,N,f):

    print(0,x0,x1)
    i=1
    h= 0.00001   #delta x para calcular a derivada de f(x)
    while i<=N:
        x= x1 - (x1-x0)*f(x1)/(f(x1)-f(x0))  

        print(i,x)
        if abs(x-x1)<tol:
            return x
        i=i + 1
        x0=x1    # redefinir x0
        x1=x     #redefinir x1

    print('o metodo fracasso depois de %d iteraciones' %N)
    
import math     
    
    # Exemplo
    
f= lambda x: x**3 + 4*x**2 - 10
print(f)
x0=1
x1=2
tol=0.0001
N=20
    
x=Secante(x0,x1,tol,N,f)
print()
print('A solcao he: ',x)
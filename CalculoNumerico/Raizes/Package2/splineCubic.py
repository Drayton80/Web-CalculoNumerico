#Spline natural
#Recebe uma lista com os valores de x e uma com os valores de f(x)
#Retorna uma lista com as expressoes formadas

from scipy.interpolate import CubicSpline

def naturalspline(x,y):
  
  size = len(x)
  a=list()
  b=list()
  c=list()
  d=list()
  s = [ ]
   
  cs = CubicSpline(x,y,bc_type='natural')
  
  #Vamos iterar pelos pontos e retornar uma lista p/ cada coeficiente
  
  for i in range(0,(size-1)):
      a.append(cs.c.item(3,i))
      b.append(cs.c.item(2,i))
      c.append(cs.c.item(1,i))
      d.append(cs.c.item(0,i))
      
  #gerando as expressoes
  
  for i in range(0,(size-1)):
        a.append(cs.c.item(3,i))
        b.append(cs.c.item(2,i))
        c.append(cs.c.item(1,i))
        d.append(cs.c.item(0,i))

  for i in range(0,(size-1)):
      x0=str(i)

      s1=(str(a[i]),'+',str(b[i]),'*(x-',x0,') +',str(c[i]),'*(x-',x0,')**2 +',str(d[i]),'*(x-',x0,')**3')
      s.append(' '.join(s1))
        
  #print(retiraZero(s))
  return s

def retiraZero(funcoes):
  no_zero_f = []
  i = 0
  for funcao in funcoes:
    no_zero = ''
    inzero = no_zero.find('0.0')
    if inzero == -1:
      while inzero == -1:
        primeiroEs = funcao.find(' ', inzero)
        no_zero += funcao[:inzero]
        no_zero += funcao[primeiroEs:]
        inzero = funcao.find('0.0')
        funcao = no_zero
        i+=1
        if i == 50:
          print("Laço infinito")
          break
    else:
      no_zero = funcao
    no_zero_f.append(no_zero)
  return no_zero_f







x_points = [ 0, 1, 2, 3, 4, 5]
y_points = [12,14,22,39,58,77]

splin = naturalspline(x_points, y_points)

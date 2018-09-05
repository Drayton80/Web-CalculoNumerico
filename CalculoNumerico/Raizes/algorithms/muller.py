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

        fp0 = evalFunction(fx, x0)
        fp1 = evalFunction(fx, x1)
        fp2 = evalFunction(fx, x2)

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

from algorithms1 import numeric_methods
# exemplo testezinho
func = numeric_methods.replace_Exponentiation('x^3 - 13 *x - 12')
print(eval('10**-3 - 2'))
result, itera = numeric_methods.muller(func,'4.5','5.5','5','0.0001')
print(result)
print(itera)
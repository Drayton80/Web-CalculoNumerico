MAX_ITER = 10 #Vai definir o limite de iterações, lembrar de substituir isso pelo critério de parada que será definido posteriormente 

#TODO: Implementar uma maneira de receber o string(provável) função da entrada do site e transformar em expressão (Importante)
#Retorna o valor da função para um parâmetro dado
def funcao( x ):
    return ((x * x * x) - (9*x) + (5))

 
# Calcula as raízes aproximadas da função no intervalo dado
def falsaPosicao(a , b):
    if funcao(a) * funcao(b) >= 0:
        print("A função deve ter sinais opostos para a e b")
        return -1
    c = a # Começa com um chute
     
    for i in range(MAX_ITER):
         
        # Achar uma aproximação
        c = (a * funcao(b) - b * funcao(a))/ (funcao(b) - funcao(a))
        print("O valor da raiz é : " , '%.4f' %c)
        print("O valor da função raiz é : " , '%.4f' %funcao(c))
         
        # Checar se o c achado já é a raiz
        if funcao(c) == 0:
            break
         
        # Decide o lado para depois repetir os passos
        elif funcao(c) * funcao(a) < 0:
            b = c
        else:
            a = c

    
    
 
# Teste da função
# Os valores aqui são assumidos
a = 0.5
b = 1
falsaPosicao(a, b)

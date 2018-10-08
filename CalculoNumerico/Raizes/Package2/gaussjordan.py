import numpy as np
import sys

def gj(lista,b):
    '''
    matriz = np.zeros((m,m))
    vetor = np.zeros((m))
    x=np.zeros((m))
    
    for r in range(0,m):
        for c in range(0,m):
            matriz[(r),(c)]=lista[r][c]
        vetor[(r)]=b[(r)]
    
    for k in range(0,m):
        t=matriz[k,k]
        if(t == 0):
            print("Matriz singular")
            sys.exit(0)
        for s in range(m):
            matriz[k,s]=matriz[k,s]/t
            if(s==m-1):
                vetor[k] = vetor[k]/t
            for r in range(m):        
                g=r
                if(k != r):
                    matriz[r,k] = matriz[r,k] - (matriz[r,k]*matriz[k,s])
                    if(r==m-1):
                        vetor[g] = vetor[g] - (vetor[g]*vetor[k])
                        
    for s in range(0,m):
        x[s]=vetor[s]/matriz[s,s]
    '''
    
    return  np.linalg.solve(lista, b).tolist()
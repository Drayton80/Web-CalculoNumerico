        
class falsaP:
        def evalFunction(f, x):
                x = eval(f)
                return x

        def falsaPosicao(fx, a, b, tol, maxI, tipoErro):
                
                maxI = int(maxI)
                a = float(a)
                b = float(b)
                tol = float(tol)
                tipoErro = tipoErro
                nIteracoes = 0
                err = 1000

                fa = falsaP.evalFunction(fx, a)
                fb = falsaP.evalFunction(fx, b)

                if falsaP.evalFunction(fx, a) * falsaP.evalFunction(fx, b) >= 0:
                        raise Exception("A função deve ter sinais opostos para a e b")
                c = a

                while (nIteracoes < maxI):
                        aux = c
                        fa = falsaP.evalFunction(fx, a)
                        fb = falsaP.evalFunction(fx, b)
                        c = ((a * fb) - (b * fa)) / (fb - fa)
                        fc = falsaP.evalFunction(fx, c)

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
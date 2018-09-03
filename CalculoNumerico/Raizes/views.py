from django.shortcuts import render

# Create your views here.
def paginaInicial(request):
	if request.method == "POST" and 'falsaPosicaoSalvar' in request.POST:
		print(request.POST)
		equacao = request.POST.get('falsaPosicaoEquacaoInput')
		LI = request.POST.get("falsaPosicaoLIInput")
		LU = request.POST.get("falsaPosicaoLSInput")
		tolerancia = request.POST.get("falsaPosicaoToleranciaInput")
		erro = request.POST.get("falsaPosicaoErro")
		print(
			'equacao:' , equacao, '\n',
			'Limite Inferior:' , LI, '\n',
			'Limte Superior:' , LU, '\n',
			'tolerancia:' , tolerancia, '\n'
			"Erro:", erro, '\n'
			)
		pass

	elif request.method == "POST" and 'secanteSalvar' in request.POST:
		print(request.POST)
		equacao = request.POST.get('secanteEquacaoInput')
		x0 = request.POST.get("secanteX0Input")
		x1 = request.POST.get("secanteX1Input")
		tolerancia = request.POST.get("falsaPosicaoToleranciaInput")
		erro = request.POST.get("secateErro")
		print(
			'equacao:' , equacao, '\n',
			'x0:' , x0, '\n',
			'x1:' , x1, '\n',
			'tolerancia:' , tolerancia, '\n',
			'Erro', erro, '\n',
			)
		pass

	elif request.method == "POST" and 'mullerSalvar' in request.POST:
		equacao = request.POST.get('mullerEquacaoInput')
		x0 = request.POST.get("mullerX0Input")
		x1 = request.POST.get("mullerX1Input")
		x2 = request.POST.get("mullerX2Input")
		tolerancia = request.POST.get("mullerToleranciaInput")
		erro = request.POST.get("mullerErro")
		print(
			'equacao:' , equacao, '\n',
			'x0:' , x0, '\n',
			'x1:' , x1, '\n',
			'x2:' , x2, '\n',
			'tolerancia:' , tolerancia, '\n',
			'Erro', erro, '\n',
			)
		pass

	contexto = {}
	return render(request, "Raizes/base.html", contexto)
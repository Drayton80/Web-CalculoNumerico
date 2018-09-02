from django.shortcuts import render

# Create your views here.
def paginaInicial(request):
	print(request)
	if request.method == "POST" and 'falsaPosicaoSalvar' in request.POST:
		print(request.POST)
		equacao = request.POST.get('falsaPosicaoEquacaoInput')
		LI = request.POST.get("falsaPosicaoLIInput")
		LU = request.POST.get("falsaPosicaoLSInput")
		tolerancia = request.POST.get("falsaPosicaoToleranciaInput")
		print(
			'equacao:' , equacao, '\n',
			'Input:' , equacao, '\n',
			'equacao:' , equacao, '\n',
			'equacao:' , equacao, '\n'
			)
	contexto = {}
	return render(request, "Raizes/base.html", contexto)
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from django.urls import reverse
from .api_mercadopago import create_payment
from .models import Sorteio
from django.core.exceptions import PermissionDenied

def homepage(request):
    numeros = Sorteio.objects.filter(aprovado=True)
    numeros_bloqueados = [num.numero_rifa for num in numeros]
    return render(request, 'homepage.html', {'my_range': range(201), 'numeros_bloqueados': numeros_bloqueados})

def comprar(request, rifa_id):
    numeros = Sorteio.objects.filter(aprovado=True)
    numeros_bloqueados = [num.numero_rifa for num in numeros]
    if rifa_id in numeros_bloqueados or rifa_id > 200:
        raise PermissionDenied
    else:
        if request.method == 'GET':
            return render(request, 'shop.html', {'rifa': rifa_id})
        elif request.method == 'POST':
            nome = request.POST.get('nome')
            sobrenome = request.POST.get('sobrenome')
            link = request.build_absolute_uri(reverse('siterifa:finalizar_pagamento') + f'?rifa_id={rifa_id}&nome={nome}&sobrenome={sobrenome}')
            link_pagamento, id_pagamento = create_payment(rifa_id, link)
            pagamento = Sorteio.objects.create(nome=nome, sobrenome=sobrenome, numero_rifa=rifa_id, aprovado=False)
            pagamento.save()
            return redirect(link_pagamento)

def pix(request):
    return render(request, 'pix.html')

def finalizar_pagamento(request):
    dados = request.GET.dict()
    status = dados.get('status')
    rifa_id = dados.get('rifa_id') 
    nome = dados.get('nome')
    sobrenome = dados.get('sobrenome')
    if status == 'approved':
        numero_escolhido = Sorteio.objects.get(numero_rifa=rifa_id)
        numero_escolhido.aprovado = True
        numero_escolhido.save()
        return redirect('siterifa:home')

    elif status == 'rejected':
        numero_escolhido = Sorteio.objects.get(numero_rifa=rifa_id)
        numero_escolhido.delete()
        return redirect('siterifa:home')
    return redirect('siterifa:home')

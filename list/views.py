# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Max
from django.core import serializers
from django.db.models import Q
from django.http import Http404

from .models import Lista

def index(request):
    lista_tarefas = Lista.objects.all().order_by('ordem_tarefa')
    context = {'tarefas': lista_tarefas}
    return render(request, 'list/index.html', context)

def adiciona_tarefa(request):
    descricao_nova_tarefa = request.GET.get('descricao_nova_tarefa', None)
    if descricao_nova_tarefa:
        ordem = (Lista.objects.all().aggregate(Max('ordem_tarefa'))['ordem_tarefa__max']) + 1
        tarefa = Lista(descricao_tarefa=descricao_nova_tarefa, ordem_tarefa=ordem)
        tarefa.save()
        data = {'tarefa_salva': True, 'id': tarefa.pk, 'descricao': tarefa.descricao_tarefa, 'ordem': tarefa.ordem_tarefa, 'status': tarefa.status_tarefa}
    else:
        data = {'tarefa_salva': False}
    return JsonResponse(data)

def reordena(request):
    ordem_tarefas = request.GET.get('ordem_tarefas', None)
    ordem_tarefas = ordem_tarefas.replace("sort=card","").split("&")
    pos = 0
    for tarefa in ordem_tarefas:
        tarefa_m = Lista.objects.get(id=tarefa)
        if tarefa_m.ordem_tarefa != pos:
            tarefa_m.ordem_tarefa = pos
            tarefa_m.save();
        pos += 1
    
    data = {'tarefas_ordenadas': True}
    return JsonResponse(data)

def salva_status(request):
    id_tarefa = request.GET.get('id_tarefa', None)
    status_tarefa = request.GET.get('status_tarefa', None)
    
    id_tarefa = id_tarefa.replace('task','')
    
    tarefa = Lista.objects.get(id=id_tarefa)
    if status_tarefa == 'feita':
        tarefa.status_tarefa = 'F'
    elif status_tarefa == 'pendente':
        tarefa.status_tarefa = 'P'
        
    tarefa.save()
    
    data = {'tarefa_salva': True}
    
    return JsonResponse(data)

def remove_tarefa(request):
    id_tarefa = request.GET.get('id_tarefa', None)
    
    tarefa = Lista.objects.get(id = id_tarefa)
    tarefa.status_tarefa = 'E'
    tarefa.save()
    
    data = {'tarefa_removida': True}
    
    return JsonResponse(data)
    
def detalhes(request):
    id_tarefa = request.GET.get('id_tarefa', None)
    tarefa = Lista.objects.get(pk=id_tarefa)
    data = {'id': id_tarefa, 'descricao': tarefa.descricao_tarefa}

    return JsonResponse(data)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
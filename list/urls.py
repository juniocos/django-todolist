from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^adiciona_tarefa/$', views.adiciona_tarefa, name='adiciona_tarefa'),
    url(r'^reordena/$', views.reordena, name='reordena'),
    url(r'^salva_status/$', views.salva_status, name='salva_status'),
    url(r'^remove_tarefa/$', views.remove_tarefa, name='remove_tarefa'),
    url(r'^detalhes/$', views.detalhes, name='detalhes'),
]
# urls.py
from django.urls import path, re_path
from .views import AnuncioDetalhadoView, AnuncioListagemView

urlpatterns = [
    path('', AnuncioListagemView.as_view(), name='anuncio-listagem'),
    path('<int:pk>/', AnuncioDetalhadoView.as_view(), name='anuncio-detalhado'),
]

from rest_framework import viewsets
from .models import Acai, Pedido, Personalizacao
from .serializers import AcaiSerializer, PedidoSerializer, PersonalizacaoSerializer

class AcaiView(viewsets.ModelViewSet):
    queryset = Acai.objects.all()
    serializer_class = AcaiSerializer


class PersonalizacaoView(viewsets.ModelViewSet):
    queryset = Personalizacao.objects.all()
    serializer_class = PersonalizacaoSerializer


class PedidoView(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
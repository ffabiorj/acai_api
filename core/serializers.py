from rest_framework import serializers
from .models import Personalizacao, Acai, Pedido


class PersonalizacaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Personalizacao
        fields = ['acai', 'personalizacao']


class AcaiSerializer(serializers.ModelSerializer):
    personalizacao = PersonalizacaoSerializer(many=True, read_only=True)

    class Meta:
        model = Acai
        fields = ['id', 'tamanho', 'sabor', 'personalizacao']


class PedidoSerializer(serializers.ModelSerializer):
    resumo = AcaiSerializer(read_only=True)

    class Meta:
        model = Pedido
        fields = ['id', 'pedido', 'resumo' ,'tempo_de_preparo', 'valor_total']
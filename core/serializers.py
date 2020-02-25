from rest_framework import serializers
from .models import Personalizacao, Acai, Pedido


class PersonalizacaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Personalizacao
        fields = ['personalizacao']


class AcaiSerializer(serializers.ModelSerializer):
    personalizacao = PersonalizacaoSerializer(many=True, read_only=True)

    class Meta:
        model = Acai
        fields = ['id', 'tamanho', 'sabor', 'personalizacao']


class PedidoSerializer(serializers.ModelSerializer):
    resumo = serializers.SerializerMethodField()
    
    def get_resumo(self, obj):
        
        return {
            'tamanho': obj.pedido.tamanho,
            'sabor': obj.pedido.sabor,
            'personalizacoes': [PersonalizacaoSerializer(instance=x).data for x in obj.pedido.personalizacao.all()],
        }


    class Meta:
        model = Pedido
        fields = ['id', 'pedido', 'resumo', 'tempo_de_preparo', 'valor_total']
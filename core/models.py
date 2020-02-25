from django.db import models

from django.db import models


class Acai(models.Model):

    tamanho = models.CharField(
        max_length=100, blank=False, null=False)
    sabor = models.CharField(
        max_length=100, blank=False, null=False)

    def __str__(self):
        return f'Sabor: {self.sabor} Tamanho: {self.tamanho}'


class Personalizacao(models.Model):

    personalizacao = models.CharField(
        max_length=100, blank=True, null=True)
    acai = models.ForeignKey(
        Acai, related_name='personalizacao', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.personalizacao


class Pedido(models.Model):

    pedido = models.ForeignKey(
        Acai, related_name='pedidos', on_delete=models.CASCADE)

    def __str__(self):
        return self.pedido.sabor

    def tempo_de_preparo(self):
        tempo = 0

        if self.pedido.sabor == 'kiwi':
            tempo += 5
        if 'paçoca' in [str(x) for x in self.pedido.personalizacao.all()]:
            tempo += 3
        elif self.pedido.tamanho == 'pequeno (300ml)':
            tempo += 5
        elif self.pedido.tamanho == 'médio (500ml)':
            tempo += 7
        elif self.pedido.tamanho == 'grande (700ml)':
            tempo += 10
        return tempo

    def valor_total(self):
        valor = 0

        if 'paçoca' in [str(x) for x in self.pedido.personalizacao.all()]:
            valor += 3
        if 'leite ninho' in [str(x) for x in self.pedido.personalizacao.all()]:
            valor += 3
        if self.pedido.tamanho == 'pequeno (300ml)':
            valor += 10
        elif self.pedido.tamanho == 'médio (500ml)':
            valor += 13
        elif self.pedido.tamanho == 'grande (700ml)':
            valor += 15
        return valor

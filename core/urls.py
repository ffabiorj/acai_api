from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('acai', views.AcaiView)
router.register('personalizacao', views.PersonalizacaoView)
router.register('pedido', views.PedidoView)

urlpatterns = [
    path('', include(router.urls))
]
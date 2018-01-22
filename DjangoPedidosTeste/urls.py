"""
Definition of urls for DjangoPedidosTeste.
"""

from datetime import datetime
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from django.conf.urls import url
import django.contrib.auth.views
from app import views

router = DefaultRouter()

router.register(r'clientes',views.ClienteView)
router.register(r'itens',views.ItemView)
router.register(r'pedidos',views.PedidoView)
router.register(r'produtos',views.ProdutoView)

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    url(r'^', include(router.urls)),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
   
    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]

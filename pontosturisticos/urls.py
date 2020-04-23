from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from pontos_turisticos.api.viewsets import PontoTuristicoViewSet
from atracoes.api.viewsets import AtracaoViewSet
from enderecos.api.viewsets import EnderecoViewSet
from avaliacoes.api.viewsets import AvaliacaoViewSet
from comentarios.api.viewsets import ComentarioViewSet
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()
router.register(r'pontoturistico', PontoTuristicoViewSet, basename = 'PontoTuristico')
router.register(r'atracao', AtracaoViewSet)
router.register(r'endereco', EnderecoViewSet)
router.register(r'avaliacao', AvaliacaoViewSet)
router.register(r'comentario', ComentarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls), 
    path('api-token-auth/', obtain_auth_token),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

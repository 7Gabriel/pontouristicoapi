from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from atracoes.models import Atracao
from atracoes.api.serializers import AtracaoSerializer

class AtracaoViewSet(ModelViewSet):

    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nome', 'descricao']
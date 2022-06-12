from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet
import json
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404
from .models import Domino
from .serializers import DominoSerializer, ListDominoSerializer
from .domino_scan import make_domino

# Create your views here.
class DominoViewSet(ModelViewSet):
    queryset = Domino.objects.all()
    serializer_class = DominoSerializer

    @action(detail=True, methods=['GET'])
    def scandomino(self, request, *args, **kwargs):
        domino = get_object_or_404(Domino, pk=self.kwargs['pk'])
        domino = make_domino(domino.domino_pic)
        return Response(ListDominoSerializer(domino).data)
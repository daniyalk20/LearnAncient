from rest_framework import generics, permissions

from content.models import Passage, Token
from content.serializers import PassageSerializer, TokenSerializer


class ReaderPassageView(generics.RetrieveAPIView):
    queryset = Passage.objects.select_related("manuscript").prefetch_related("tokens")
    serializer_class = PassageSerializer
    permission_classes = [permissions.AllowAny]


class ReaderTokenView(generics.RetrieveAPIView):
    queryset = Token.objects.select_related("passage", "lemma", "morphology")
    serializer_class = TokenSerializer
    permission_classes = [permissions.AllowAny]

from django.shortcuts import render

# Create your views here.

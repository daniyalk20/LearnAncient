from rest_framework import generics, permissions

from .models import Passage
from .serializers import PassageSerializer


class PassageDetailView(generics.RetrieveAPIView):
    queryset = Passage.objects.select_related("manuscript").prefetch_related("tokens")
    serializer_class = PassageSerializer
    permission_classes = [permissions.AllowAny]

from django.shortcuts import render

# Create your views here.

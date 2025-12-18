from rest_framework import generics, permissions

from .models import Language, LanguagePack
from .serializers import LanguageSerializer, LanguagePackSerializer


class LanguageListView(generics.ListAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = [permissions.AllowAny]


class LanguagePackListView(generics.ListAPIView):
    serializer_class = LanguagePackSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        language_id = self.kwargs["language_id"]
        return LanguagePack.objects.filter(language_id=language_id, is_active=True)

from django.shortcuts import render

# Create your views here.

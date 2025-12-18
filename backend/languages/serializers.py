from rest_framework import serializers

from .models import Language, LanguagePack


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ["id", "code", "name", "direction", "script"]


class LanguagePackSerializer(serializers.ModelSerializer):
    language = LanguageSerializer(read_only=True)

    class Meta:
        model = LanguagePack
        fields = ["id", "language", "version", "features", "is_active"]


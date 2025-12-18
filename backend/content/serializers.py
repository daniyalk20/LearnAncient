from rest_framework import serializers

from .models import Manuscript, Passage, Token, Lemma, Morphology


class LemmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lemma
        fields = ["id", "lemma", "gloss"]


class MorphologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Morphology
        fields = ["id", "tag", "description"]


class TokenSerializer(serializers.ModelSerializer):
    lemma = LemmaSerializer(read_only=True)
    morphology = MorphologySerializer(read_only=True)

    class Meta:
        model = Token
        fields = [
            "id",
            "index",
            "text",
            "lemma",
            "morphology",
            "gloss",
            "audio_url",
        ]


class ManuscriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manuscript
        fields = ["id", "title", "description", "image_url"]


class PassageSerializer(serializers.ModelSerializer):
    manuscript = ManuscriptSerializer(read_only=True)
    tokens = TokenSerializer(many=True, read_only=True)

    class Meta:
        model = Passage
        fields = [
            "id",
            "reference",
            "content",
            "manuscript",
            "tokens",
        ]


from django.core.management.base import BaseCommand

from languages.models import Language, LanguagePack
from content.models import Manuscript, Passage, Lemma, Morphology, Token


class Command(BaseCommand):
    help = "Seed a minimal Biblical Greek language, pack, and sample passage"

    def handle(self, *args, **options):
        language, _ = Language.objects.get_or_create(
            code="biblical-greek",
            defaults={
                "name": "Biblical Greek",
                "direction": "ltr",
                "script": "Greek",
            },
        )

        pack, _ = LanguagePack.objects.get_or_create(
            language=language,
            version="1.0.0",
            defaults={
                "features": {
                    "morphology": True,
                    "audio": False,
                    "manuscripts": True,
                },
                "is_active": True,
            },
        )

        manuscript, _ = Manuscript.objects.get_or_create(
            title="Sample John 1:1 Manuscript",
            defaults={
                "description": "Demo manuscript image placeholder for John 1:1.",
                "image_url": "https://example.com/manuscripts/john1_1.png",
            },
        )

        lemma_logos, _ = Lemma.objects.get_or_create(
            language=language,
            lemma="λόγος",
            defaults={"gloss": "word"},
        )
        lemma_en, _ = Lemma.objects.get_or_create(
            language=language,
            lemma="ἐν",
            defaults={"gloss": "in"},
        )
        lemma_archē, _ = Lemma.objects.get_or_create(
            language=language,
            lemma="ἀρχή",
            defaults={"gloss": "beginning"},
        )

        morph_noun, _ = Morphology.objects.get_or_create(
            language=language,
            tag="N-NSF",
            defaults={"description": "Noun, nominative singular feminine"},
        )
        morph_prep, _ = Morphology.objects.get_or_create(
            language=language,
            tag="PREP",
            defaults={"description": "Preposition"},
        )

        passage, _ = Passage.objects.get_or_create(
            language_pack=pack,
            reference="John 1:1 (sample)",
            defaults={
                "manuscript": manuscript,
                "content": "Ἐν ἀρχῇ ἦν ὁ Λόγος",
                "is_published": True,
            },
        )

        if not passage.tokens.exists():
            surface_tokens = [
                ("Ἐν", lemma_en, morph_prep, "in"),
                ("ἀρχῇ", lemma_archē, morph_noun, "beginning"),
                ("ἦν", None, None, "was"),
                ("ὁ", None, None, "the"),
                ("Λόγος", lemma_logos, morph_noun, "Word"),
            ]

            for index, (text, lemma, morph, gloss) in enumerate(surface_tokens, start=1):
                Token.objects.create(
                    passage=passage,
                    index=index,
                    text=text,
                    lemma=lemma,
                    morphology=morph,
                    gloss=gloss,
                )

        self.stdout.write(self.style.SUCCESS("Biblical Greek seed data created/updated."))

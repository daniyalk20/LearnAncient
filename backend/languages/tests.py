from django.core.management import call_command
from django.test import Client, TestCase

from .models import Language, LanguagePack


class LanguageApiTests(TestCase):
	def setUp(self) -> None:
		# Seed Biblical Greek data so the API has something to return
		call_command("seed_biblical_greek")
		self.client = Client()

	def test_languages_endpoint_lists_language(self) -> None:
		response = self.client.get("/api/v1/languages")
		self.assertEqual(response.status_code, 200)
		data = response.json()
		self.assertGreaterEqual(len(data), 1)
		codes = {row["code"] for row in data}
		self.assertIn("biblical-greek", codes)

	def test_language_packs_endpoint_lists_pack(self) -> None:
		language = Language.objects.get(code="biblical-greek")
		response = self.client.get(f"/api/v1/languages/{language.id}/packs")
		self.assertEqual(response.status_code, 200)
		data = response.json()
		self.assertGreaterEqual(len(data), 1)
		versions = {row["version"] for row in data}
		self.assertIn("1.0.0", versions)


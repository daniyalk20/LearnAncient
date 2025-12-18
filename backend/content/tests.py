from django.core.management import call_command
from django.test import Client, TestCase

from .models import Passage


class ReaderApiTests(TestCase):
	def setUp(self) -> None:
		call_command("seed_biblical_greek")
		self.client = Client()

	def test_reader_passage_returns_tokens(self) -> None:
		passage = Passage.objects.first()
		self.assertIsNotNone(passage)
		response = self.client.get(f"/api/v1/reader/passage/{passage.id}")
		self.assertEqual(response.status_code, 200)
		data = response.json()
		self.assertIn("tokens", data)
		self.assertGreaterEqual(len(data["tokens"]), 1)


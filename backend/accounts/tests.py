from django.contrib.auth.models import User
from django.test import Client, TestCase


class AuthEndpointsTests(TestCase):
	def setUp(self) -> None:
		self.client = Client()
		self.user = User.objects.create_user(username="tester", password="pass1234")

	def test_login_returns_jwt_tokens(self) -> None:
		response = self.client.post(
			"/api/v1/auth/login",
			{"username": "tester", "password": "pass1234"},
			content_type="application/json",
		)
		self.assertEqual(response.status_code, 200)
		data = response.json()
		self.assertIn("access", data)
		self.assertIn("refresh", data)


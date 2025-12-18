from django.contrib.auth.models import User
from django.db import transaction
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .models import UserProfile


class LoginView(TokenObtainPairView):
	"""JWT login endpoint mapped to /auth/login."""


class RefreshView(TokenRefreshView):
	"""JWT refresh endpoint mapped to /auth/refresh."""


class GuestUpgradeView(APIView):
	"""Upgrade a guest/anonymous learner to a full account.

	For MVP, this creates a new User and associated UserProfile,
	returning a JWT pair. Migration of anonymous progress can be
	added later.
	"""

	permission_classes = [permissions.AllowAny]

	@transaction.atomic
	def post(self, request, *args, **kwargs):
		username = request.data.get("username")
		password = request.data.get("password")
		if not username or not password:
			return Response(
				{"detail": "username and password are required"},
				status=status.HTTP_400_BAD_REQUEST,
			)

		if User.objects.filter(username=username).exists():
			return Response(
				{"detail": "username already exists"},
				status=status.HTTP_400_BAD_REQUEST,
			)

		user = User.objects.create_user(username=username, password=password)
		UserProfile.objects.create(user=user)

		# Issue tokens using SimpleJWT's token view
		token_view = TokenObtainPairView.as_view()
		return token_view(request._request)


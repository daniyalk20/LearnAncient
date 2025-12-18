from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from content.models import Passage, Token
from content.serializers import PassageSerializer, TokenSerializer


class GlobalSearchView(APIView):
	"""Simple accent-insensitive, transliteration-agnostic search stub.

	For MVP this performs a basic icontains search over passages and tokens.
	A PostgreSQL full-text implementation can replace this later.
	"""

	permission_classes = [permissions.AllowAny]

	def get(self, request, *args, **kwargs):
		query = request.query_params.get("q")
		if not query:
			return Response(
				{"detail": "q parameter is required"},
				status=status.HTTP_400_BAD_REQUEST,
			)

		passages = Passage.objects.filter(content__icontains=query)[:20]
		tokens = Token.objects.filter(text__icontains=query)[:20]

		return Response(
			{
				"passages": PassageSerializer(passages, many=True).data,
				"tokens": TokenSerializer(tokens, many=True).data,
			}
		)


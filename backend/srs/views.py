from datetime import date

from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ReviewItem


class ReviewDueView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        today = date.today()
        items = (
            ReviewItem.objects.select_related("token", "token__passage")
            .filter(user=request.user, due__lte=today)
            .order_by("due")[:50]
        )
        data = [
            {
                "id": item.id,
                "token_id": item.token_id,
                "text": item.token.text,
                "passage_reference": item.token.passage.reference,
                "due": item.due,
            }
            for item in items
        ]
        return Response({"items": data})


class ReviewAnswerView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        item_id = request.data.get("item_id")
        quality = int(request.data.get("quality", 3))
        try:
            item = ReviewItem.objects.get(id=item_id, user=request.user)
        except ReviewItem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # Very simple SM-2–like update (placeholder for full algorithm)
        if quality < 3:
            item.repetitions = 0
            item.interval = 1
        else:
            item.repetitions += 1
            if item.repetitions == 1:
                item.interval = 1
            elif item.repetitions == 2:
                item.interval = 6
            else:
                item.interval = int(item.interval * item.easiness)
        item.due = date.today().fromordinal(date.today().toordinal() + item.interval)
        item.save()

        return Response({"next_due": item.due})

from django.shortcuts import render

# Create your views here.

from django.urls import path

from .views import ReviewDueView, ReviewAnswerView


urlpatterns = [
    path("review/due", ReviewDueView.as_view(), name="review-due"),
    path("review/answer", ReviewAnswerView.as_view(), name="review-answer"),
]

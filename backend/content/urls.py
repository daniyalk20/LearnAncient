from django.urls import path

from .views import PassageDetailView


urlpatterns = [
    path("passages/<int:pk>", PassageDetailView.as_view(), name="passage-detail"),
]

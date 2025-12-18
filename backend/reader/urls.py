from django.urls import path

from .views import ReaderPassageView, ReaderTokenView


urlpatterns = [
    path("reader/passage/<int:pk>", ReaderPassageView.as_view(), name="reader-passage"),
    path("reader/token/<int:pk>", ReaderTokenView.as_view(), name="reader-token"),
]

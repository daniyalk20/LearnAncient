from django.urls import path

from .views import LanguageListView, LanguagePackListView


urlpatterns = [
    path("languages", LanguageListView.as_view(), name="language-list"),
    path(
        "languages/<int:language_id>/packs",
        LanguagePackListView.as_view(),
        name="language-pack-list",
    ),
]

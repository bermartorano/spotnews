from .views import inicial_page, details_page, register_category, register_news
from django.urls import path


urlpatterns = [
    path("", inicial_page, name="home-page"),
    path("news/<int:id>", details_page, name="news-details-page"),
    path("categories", register_category, name="categories-form"),
    path("news", register_news, name="news-form"),
]

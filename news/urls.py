from .views import inicial_page, details_page
from django.urls import path


urlpatterns = [
    path("", inicial_page, name="home-page"),
    path("news/<int:id>", details_page, name="news-details-page")
]

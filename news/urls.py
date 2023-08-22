from .views import inicial_page
from django.urls import path


urlpatterns = [
    path("", inicial_page, name="home-page")
]

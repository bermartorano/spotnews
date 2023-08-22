from django.shortcuts import render
from .models.news_model import News


def inicial_page(request):
    context = {"news": News.objects.all()}
    return render(request, "home.html", context)

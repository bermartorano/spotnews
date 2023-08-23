from django.shortcuts import render
from .models.news_model import News


def inicial_page(request):
    context = {"news": News.objects.all()}
    return render(request, "home.html", context)


def details_page(request, id):
    news = News.objects.get(id=id)
    context = {"news": news}
    return render(request, "news_details.html", context)

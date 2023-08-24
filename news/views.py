from django.shortcuts import render, redirect
from .models.news_model import News
from .forms.category_form import CreateCategoryModelForm
from .forms.news_form import CreateNewsModelForm
from .models.category_model import Categories


def inicial_page(request):
    context = {"news": News.objects.all()}
    return render(request, "home.html", context)


def details_page(request, id):
    news = News.objects.get(id=id)
    context = {"news": news}
    return render(request, "news_details.html", context)


def register_category(request):
    if request.method == "POST":
        form = CreateCategoryModelForm(request.POST)

        if form.is_valid():
            Categories.objects.create(**form.cleaned_data)
            return redirect("home-page")

    form = CreateCategoryModelForm()
    context = {"form": form}
    return render(request, "categories_form.html", context)


def register_news(request):
    if request.method == "POST":
        form = CreateNewsModelForm(request.POST, request.FILES)
        print('********', request.FILES)

        if form.is_valid():
            form_to_create = {**form.cleaned_data}
            form_to_create.pop("categories")
            news = News(**form_to_create)
            news.save()
            news.categories.add(form.cleaned_data["categories"][0])
            return redirect("home-page")

    form = CreateNewsModelForm()
    context = {"form": form}
    return render(request, "news_form.html", context)

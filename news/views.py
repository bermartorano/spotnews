from django.shortcuts import render, redirect
from .models.news_model import News
from .forms.category_form import CreateCategoryModelForm
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

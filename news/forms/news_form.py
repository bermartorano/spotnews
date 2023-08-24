from django import forms
from ..models.news_model import News


class CreateNewsModelForm(forms.ModelForm):
    class Meta:
        model = News
        fields = "__all__"
        widgets = {'categories': forms.CheckboxSelectMultiple}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].label = "Título"
        self.fields["content"].label = "Conteúdo"
        self.fields["author"].label = "Autoria"
        self.fields["created_at"].label = "Criado em"
        self.fields["created_at"].widget = forms.DateInput(
            attrs={"type": "date"})
        self.fields["image"].label = "URL da Imagem"
        self.fields["content"].label = "Conteúdo"
        self.fields["categories"].label = "Categorias"

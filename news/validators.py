from django.core.exceptions import ValidationError


def word_count_validator(text: str):
    if len(text.split()) < 2:
        raise ValidationError("O título deve conter pelo menos 2 palavras.")
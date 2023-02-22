from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope


class ArticleInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_entry = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                main_entry += 1
        if main_entry == 0:
            raise ValidationError('Укажите один основной раздел')
        elif main_entry > 1:
            raise ValidationError('Основной раздел может быть только один')
        return super().clean()  # вызываем базовый код переопределяемого метода

# class ScopeInline(admin.TabularInline):
#     model = Scope
#     extra = 0
#     formset = ScopeInlineFormset

class ArticleInline(admin.TabularInline):
    model = Article.scopes.through
    extra = 0
    formset = ArticleInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleInline,]

@admin.register(Tag)
class TagsAdmin(admin.ModelAdmin):
    pass
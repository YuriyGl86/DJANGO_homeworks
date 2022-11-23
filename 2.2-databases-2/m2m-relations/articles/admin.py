from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):

        is_main_list = [form.cleaned_data.get('is_main', False) for form in self.forms]
        is_main_counter = sum(is_main_list)
        print('список is_main', is_main_list, 'счетчик', is_main_counter)

        if is_main_counter > 1:
            raise ValidationError('Основным может быть только один раздел')
        elif not is_main_counter:
            raise ValidationError('Укажите основной раздел')

        return super().clean()  # вызываем базовый код переопределяемого метода


class ScopesInline(admin.TabularInline):
    model = Scope
    extra = 1
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at')
    inlines = [ScopesInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']


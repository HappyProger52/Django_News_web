from django import forms

from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'title',
            'short_description',
            'description',
            'preview_image',
            'full_image',
            'published_at',
        ]

        labels = {
            'title': 'Заголовок новости',
            'short_description': 'Краткое описание',
            'description': 'Полное описание',
            'preview_image': 'Изображение-превью',
            'full_image': 'Полное изображение',
            'published_at': 'Дата публикации',
        }

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите заголовок новости'
            }),
            'short_description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите краткое описание',
                'rows': 4
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите полное описание',
                'rows': 7
            }),
            'preview_image': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Например: preview.jpg'
            }),
            'full_image': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Например: full.jpeg'
            }),
            'published_at': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')

        if len(title) < 5:
            raise forms.ValidationError(
                'Заголовок должен содержать минимум 5 символов.'
            )

        return title

    def clean_short_description(self):
        short_description = self.cleaned_data.get('short_description')

        if len(short_description) < 10:
            raise forms.ValidationError(
                'Краткое описание должно содержать минимум 10 символов.'
            )

        return short_description

    def clean_description(self):
        description = self.cleaned_data.get('description')

        if len(description) < 20:
            raise forms.ValidationError(
                'Полное описание должно содержать минимум 20 символов.'
            )

        return description
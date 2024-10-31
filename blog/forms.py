from django import forms

from blog.models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'image']
        labels = {
            'title': 'Заголовок статьи',
            'content': 'Содержимое статьи',
            'created_at': 'Дата создания',
            'image': 'Изображение',
        }
        widgets = {
            'created_at': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        help_texts = {
            'title': 'Максимальная длина заголовка - 200 символов.',
            'content': 'Максимальный объем текста - 10000 символов.',
        }
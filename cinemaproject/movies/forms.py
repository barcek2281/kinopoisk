# forms.py
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'is_positive']
        widgets = {
            'text': forms.Textarea(attrs={'placeholder': 'Ваш комментарий', 'rows': 4, 'cols': 40}),
            'is_positive': forms.Select(choices=[(True, 'Положительный'), (False, 'Отрицательный')]),
        }
        label = {
            'content': 'Комментарий',
            'is_positive': 'Положительный',
        }

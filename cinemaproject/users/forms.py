from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

class UserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''  # Убираем стандартный help_text для поля password1
        self.fields['password2'].help_text = ''
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username',  'password1', 'password2',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Введите ваше имя'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Введите вашу фамилию'}),
            'username': forms.TextInput(attrs={'placeholder': 'Введите ваше имя пользователя'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Введите ваш email'}),
        }
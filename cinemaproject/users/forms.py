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

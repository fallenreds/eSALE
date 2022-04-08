from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, forms, AuthenticationForm

class UserCreationForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.Textarea(attrs= {'class': 'inputarea'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs= {'class': 'input'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs= {'class': 'input'}))
    class Meta(UserCreationForm.Meta):
        #переопределяем стандартного пользователя на нашего
        model = get_user_model()


class AuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'inputarea'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'input'}))




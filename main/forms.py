from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, forms, AuthenticationForm

class UserCreationForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs= {'class': 'inputarea', 'placeholder':'Логин'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs= {'class': 'inputarea', 'placeholder':'Пароль'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs= {'class': 'inputarea','placeholder':'Повторите пароль'}))
    first_name = forms.CharField(label='имя', widget=forms.TextInput(attrs= {'class': 'inputarea','placeholder':'Имя'}))
    last_name = forms.CharField(label='имя', widget=forms.TextInput(attrs= {'class': 'inputarea','placeholder':'Фамилия'}))
    email = forms.EmailField(label='Почти', widget=forms.EmailInput(attrs= {'class': 'inputarea', 'placeholder':'Почта'}))

    class Meta(UserCreationForm.Meta):
        #переопределяем стандартного пользователя на нашего
        model = get_user_model()


class MyAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'inputarea','placeholder':'Логин'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'inputarea','placeholder':'Пароль'}))




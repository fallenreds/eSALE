from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, forms, AuthenticationForm

from .category_interface import list_categories
from .forms_interface import create_post
from .models import Post, Category, Comment


class MyUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label="Логин", widget=forms.TextInput(attrs={"class": "inputarea", "placeholder": "Логин"})
    )
    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={"class": "inputarea", "placeholder": "Пароль"}),
    )
    password2 = forms.CharField(
        label="Повторите пароль",
        widget=forms.PasswordInput(attrs={"class": "inputarea", "placeholder": "Повторите пароль"}),
    )
    first_name = forms.CharField(
        label="имя", widget=forms.TextInput(attrs={"class": "inputarea", "placeholder": "Имя"})
    )
    last_name = forms.CharField(
        label="имя", widget=forms.TextInput(attrs={"class": "inputarea", "placeholder": "Фамилия"})
    )
    email = forms.EmailField(
        label="Почти", widget=forms.EmailInput(attrs={"class": "inputarea", "placeholder": "Почта"})
    )

    class Meta(UserCreationForm.Meta):
        # переопределяем стандартного пользователя на нашего
        model = get_user_model()
        fields = ["username", "password1", "first_name", "last_name", "email"]


class MyAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label="Логин", widget=forms.TextInput(attrs={"class": "inputarea", "placeholder": "Логин"})
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={"class": "inputarea", "placeholder": "Пароль"}),
    )


class NewPostForm(forms.Form):
    title = forms.CharField(
        label="Заголовок",
        widget=forms.TextInput(attrs={"placeholder": "Заголовок", "class": "inputarea"}),
    )
    text = forms.CharField(
        label="Описание",
        widget=forms.Textarea(
            attrs={"placeholder": "Описание", "class": "descrip", "maxlength": "300"}
        ),
    )
    cost = forms.FloatField(
        label="Цена",
        widget=forms.NumberInput(attrs={"placeholder": "Цена", "min": "1", "class": "inputarea"}),
    )
    category = forms.ChoiceField(
        choices=list_categories()
        # queryset=None, widget=forms.Select(attrs={"class": "inputarea"})
    )

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['category'].queryset = list_categories()

    def save(self, author_id):
        create_post(self.cleaned_data, author_id=author_id)


class CreateCommentForm(forms.ModelForm):
    text = forms.CharField(
        label="Коментарий",
        widget=forms.Textarea(
            attrs={
                "placeholder": "Напишите ваш коментарий о пользователе",
                "class": "descrip",
                "maxlength": "300",
            }
        ),
    )

    class Meta:
        model = Comment
        fields = ("text",)

from django.contrib.auth.forms import UserCreationForm
from django import forms
from . import models


class SignUpForm(UserCreationForm):
    class Meta:
        model = models.User
        fields = ('username', 'email', 'password1')
        #widgets = {
        #    'password1': forms.PasswordInput(attrs={'placeholder': 'パスワード'}),
        #}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs = {'placeholder': 'ユーザー名'}
        # self.fields["username"].help_text = "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."

        self.fields["email"].required = True
        self.fields["email"].widget.attrs = {'placeholder': 'メールアドレス'}
        self.fields["password1"].widget.attrs = {'placeholder': 'パスワード'}
        self.fields["password2"].widget.attrs = {'placeholder': '確認⽤パスワード'}


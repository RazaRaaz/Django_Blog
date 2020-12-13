from django import forms


class RegisterForm(forms.Form):
       user_name = forms.CharField(label='User Name', max_length=4000)
       email = forms.EmailField()
       password = forms.CharField(widget=forms.PasswordInput())
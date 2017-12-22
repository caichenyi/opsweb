from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group form-control', 'placeholder': '用户名'}), label='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-group form-control', 'placeholder': '密码'}), label='')

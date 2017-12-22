from django import forms

from . import models, sqlcheck

class CreateDBForm(forms.Form):
    db_env = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group form-control', 'placeholder': '识别名'}), label='识别名')
    db_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group form-control', 'placeholder': '数据库名'}), label='数据库名')
    db_host = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group form-control', 'placeholder': 'host'}), label='host')
    db_port = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'input-group form-control', 'placeholder': 'port'}), label='port')
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group form-control', 'placeholder': '用户名'}), label='用户名')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-group form-control', 'placeholder': '密码'}), label='密码')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-group form-control', 'placeholder': '确认密码'}), label='确认密码')

    def clean_password2(self):
        password = self.cleaned_data.get('password', '')
        password2 = self.cleaned_data.get('password2', '')
        if password != password2:
            raise forms.ValidationError('两次密码不一致')
        return password2


class SubmitSqlForm(forms.Form):
    db_env = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'input-group form-control'}), queryset=models.DbEnv.objects.all(), label='数据库')
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group form-control'}), label='标题名')
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'input-group form-control'}), label='sql 内容')

    def clean_content(self):
        db_env = self.cleaned_data.get('db_env', '')
        content = self.cleaned_data.get('content', '')
        if not sqlcheck.sql_selfreview(db_env, content):
            raise forms.ValidationError('sql自检失败')
        else:
            return content
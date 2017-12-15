from django import forms

class SubmitForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group form-control'}), label='标题名', error_messages={'request': '标题名不能为空'})
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'input-group form-control'}), label='sql 内容', error_messages={'request': 'sql 语句不能为空'})

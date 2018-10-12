#__anthor:  "xuchen:
#date:   2018/2/6
from django import forms
from django.forms import fields,widgets
class RegisterForm(forms.Form):
    username=forms.CharField()
    email=forms.EmailField()
    email_code=forms.CharField()
    password=forms.CharField(widget=widgets.PasswordInput)


class SendMsgForm(forms.Form):
    email=forms.EmailField()

class LoginForm(forms.Form):
    user=forms.CharField()
    pwd=forms.CharField()
    code=forms.CharField()




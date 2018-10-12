#__anthor:  "xuchen:
#date:   2018/2/3
from django.forms import Form
from django.forms import widgets
from django.forms import fields

class MyForm(Form):
    user=fields.CharField(max_length=6 ,error_messages={'required':'用户名不能为空','min_length':'用户名长度不能小于6'})
    email=fields.EmailField(error_messages={'required':'邮箱不能为空','invalid': '邮箱格式错误'})
    # pwd=fields.CharField(widget=widgets.PasswordInput(attrs={'class':'c1'},render_value=True))
    # gender=fields.ChoiceField(choices=((1,'男'),(2,'女'),),initial=2,widget=widgets.RadioSelect)
    # city=fields.CharField(initial=2,widget=widgets.SelectMultiple(
    #     choices=((1,'sh'),(2,'bj'),(3,'nj'),)
    # ))
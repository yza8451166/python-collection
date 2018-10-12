from django.db import models

# Create your models here.

class SendMsg(models.Model):
    nid=models.AutoField(primary_key=True)
    code=models.CharField(max_length=6)
    email=models.EmailField(max_length=32,db_index=True)
    times=models.IntegerField(default=0)
    ctime=models.DateTimeField()

class UserInfo(models.Model):
    nid=models.AutoField(primary_key=True)
    username=models.CharField(max_length=32,unique=True)
    password=models.CharField(max_length=32)
    email=models.EmailField(max_length=32,unique=True)
    ctime=models.DateTimeField()

# class NewsType(models.Model):
#     caption=models.CharField(max_length=16)

class News(models.Model):
    title=models.CharField(max_length=64)
    summary=models.CharField(max_length=128,null=True)
    url=models.URLField(null=True)
    ctime=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(to='UserInfo',to_field='nid',related_name='n',on_delete=models.CASCADE)
    news_type_choices = [(1, '42区'), (2, '段子'), (3, '图片'), (4, '挨踢1024'), (5, '你问我答'), ]
    nt = models.IntegerField(choices=news_type_choices)
    comment_count=models.IntegerField(default=0)
    favor_count=models.IntegerField(default=0)
    favor = models.ManyToManyField(to='UserInfo')



# class Favor(models.Model):
#     user=models.ForeignKey(to='UserInfo',to_field='nid')
#     news=models.ForeignKey(to='News',to_fields='id')
class Comment(models.Model):
    news=models.ForeignKey(to='News',to_field='id',on_delete=models.CASCADE)
    user=models.ForeignKey(to='UserInfo',to_field='nid',on_delete=models.CASCADE)
    content=models.CharField(max_length=150)
    device=models.CharField(max_length=16,null=True)
    ctime=models.DateTimeField(auto_now_add=True)
    parent_comment=models.ForeignKey(to='self',null=True,related_name='p',on_delete=models.CASCADE)


class Test(models.Model):
    name=models.CharField(max_length=16)
    email=models.EmailField(max_length=32)
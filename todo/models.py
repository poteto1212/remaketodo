from django.db import models


class TodoModel(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    #ユーザーリストを外部キーとする
    pic=models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
        )
        
    category=models.CharField(max_length=50,blank=True,null=True)
# Create your models here.

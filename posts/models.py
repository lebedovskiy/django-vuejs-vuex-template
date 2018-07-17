from django.db import models

# Create your models here.


class Post(models.Model):
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)



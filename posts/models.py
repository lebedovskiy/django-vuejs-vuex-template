from django.db import models

# Create your models here.


class Post(models.Model):
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_date']


class Presentation(models.Model):
    owner = models.ForeignKey('auth.User', related_name='presentation', on_delete=models.CASCADE)
    phone = models.CharField(max_length=25, default='+79089353416')
    e_mail = models.CharField(max_length=30, default='lebedevegor1996@yandex.ru')
    language = models.CharField(max_length=90, default='Владение языками: русский – родной, английский – '
                                                       'разговорный/чтение технической документации.')
    stack = models.CharField(max_length=70, default='Django 2.0 (Backend Framework)  + Python 3.6 + PostgreSQL + nginx')
    skills = models.TextField()
    education = models.CharField(max_length=70, default='Среднее')
    title = models.CharField(max_length=250)
    text = models.TextField()
    salary = models.CharField(max_length=15, default='25000 руб.')


class Main(models.Model):
    owner = models.ForeignKey('auth.User', related_name='main', on_delete=models.CASCADE)
    title = models.TextField()
    subtitle = models.TextField()
    text = models.TextField()

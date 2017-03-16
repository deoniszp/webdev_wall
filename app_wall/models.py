from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    user = models.ForeignKey(User)
    text = models.TextField(verbose_name='Message text', null=False)
    date_pub = models.DateTimeField(verbose_name='Date publication', auto_now_add=True, null=False)

    class Meta:
        db_table = 'messages'
        ordering = ['-date_pub']

class Comment(models.Model):
    message = models.ForeignKey(Message, null=False)
    parent = models.ForeignKey('self', null=True, blank=True)
    user = models.ForeignKey(User)
    text = models.TextField(verbose_name='Message text', null=False)
    date_pub = models.DateTimeField(verbose_name='Date publication', auto_now_add=True, null=False)

    class Meta:
        db_table = 'comments'
        ordering = ['date_pub']

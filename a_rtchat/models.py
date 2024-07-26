from django.db import models
from django.contrib.auth.models import User
import shortuuid
# Create your models here.

class ChatGroup(models.Model):
    group_name = models.CharField(max_length=128, unique=True)
    users_online = models.ManyToManyField(User, related_name='online_in_groups', blank=True)
    members = models.ManyToManyField(User, related_name='chat_groups', blank=True)
    is_private = models.BooleanField(default=False)

    def __str__(self):
        return self.group_name

    def save(self, *args, **kwargs):
        if not self.group_name:
            self.group_name = shortuuid.uuid()
        super().save(*args, **kwargs)

class GroupMessage(models.Model):
    group =models.ForeignKey(ChatGroup, related_name=("chat_message"), on_delete=models.CASCADE)
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    body=models.CharField(max_length=300)
    created=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.author.username} : {self.body}'
    

    class Meta:
        ordering = ['-created']
from django.db import models
from users.models import User


# Create your models here.
ACTION_CHOICES = (
    ('like', "Like"),
    ('saved', "Saved"),
    ('view', "View"),
)


class Post(models.Model):
    repost = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    media = models.FileField(upload_to="post_media/")
    likes = models.PositiveBigIntegerField(default=0)
    saveds = models.PositiveBigIntegerField(default=0)
    reposts = models.PositiveBigIntegerField(default=0)
    views = models.PositiveBigIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.body
    

class Action(models.Model):
    action_type = models.CharField(max_length=25, choices=ACTION_CHOICES)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE) 
    datetime = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.action_type)
    
    
class Notification(models.Model):
    body = models.CharField(max_length=300)
    datetime = models.DateTimeField(auto_now_add=True)
    is_seen = models.BooleanField(default=False)
    to = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.body)
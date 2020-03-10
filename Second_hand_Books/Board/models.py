from django.db import models
from django.contrib.auth.models import User
import os
from django.conf import settings

# Create your models here.

def images_path():
    return os.path.join(settings.LOCAL_FILE_DIR, 'images')

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    create_by = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    text_book = models.CharField(null=False, blank=False, max_length=180)

    BUY = '1'
    SELL = '2'
    TYPES = (
        (BUY, 'buyer'),
        (SELL, 'seller')
    )

    post_type = models.CharField(max_length=2, choices=TYPES, default='1')
    price = models.FloatField(null=False, blank=False)
    picture = models.FilePathField(null=False, blank=True, path=images_path)
    OPEN = '1'
    CLOSED = '2'
    STATUS = (
        (OPEN, 'Post Opened'),
        (CLOSED, 'Post Closed')
    )

    pose_status = models.CharField(max_length=2, choices=STATUS, default='1')

    def __str__(self):
        return '(%s)' % (self.text_book)

class Message(models.Model):
    id = models.AutoField(primary_key=True)
    message = models.CharField(max_length=255)
    create_date = models.DateTimeField(auto_now=True)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    create_by = models.ForeignKey(User, on_delete=models.CASCADE)
from __future__ import unicode_literals
from django_comments.moderation import CommentModerator, moderator
from django.db import models

# Create your models here.

class Group(model.Models):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    enable_comments = models.BooleanField(default=True)

    def __unicode__(self):
        return str(self.name)

class Post(model.Models):
    group = models.ForeignKey(Group)
    body = models.TextField(max_length=150)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return str(self.name)

class Group_Moderator(CommentModerator):
    enable_field = 'enable_comments'

moderator.register(Group, Group_Moderator)

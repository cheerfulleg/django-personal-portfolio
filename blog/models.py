from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=30)
    date_posted = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

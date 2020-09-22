from django.db import models
from django_resized import ResizedImageField


class Project(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    image = ResizedImageField(size=[243, 136], crop=['top', 'left'], upload_to='portfolio/img/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

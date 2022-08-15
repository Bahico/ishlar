from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=600)
    photo = models.ImageField()
    date = models.CharField(max_length=10)
    like = models.IntegerField()
    dislike = models.IntegerField()
    views = models.IntegerField()

    def __str__(self):
        return self.title

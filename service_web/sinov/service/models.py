from django.db import models


class Task(models.Model):
    description = models.CharField(max_length=600)
    photo = models.ImageField()
    date = models.CharField(max_length=10)
    like = models.IntegerField()
    dislike = models.IntegerField()
    views = models.IntegerField()
    author = models.IntegerField()

    def __str__(self):
        return self.description


class Like(models.Model):
    post_id = models.IntegerField()
    author = models.IntegerField()


class DisLike(models.Model):
    post_id = models.IntegerField()
    author = models.IntegerField()

from django.db import models


# Create your models here.


class Comment(models.Model):
    post_id = models.IntegerField()
    description = models.TextField()
    author = models.IntegerField()
    username = models.CharField(max_length=17)

    def __str__(self):
        return self.author

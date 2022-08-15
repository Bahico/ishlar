from django.db import models


# Create your models here.


class Comment(models.Model):
    post_id = models.IntegerField()
    full_name = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='comment', blank=True)

    def __str__(self):
        return self.full_name

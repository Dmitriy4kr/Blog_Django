from django.db import models


class PostTitle(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('post_author.PostAuthor', on_delete=models.CASCADE)
    published_date = models.DateField()

    def __str__(self):
        return self.title
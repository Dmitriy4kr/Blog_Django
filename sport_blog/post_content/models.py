from django.db import models


class PostContent(models.Model):
    title = models.OneToOneField('post_title.PostTitle', on_delete=models.CASCADE)
    content_text = models.TextField()

    def __str__(self):
        return f"Content for {self.title}"
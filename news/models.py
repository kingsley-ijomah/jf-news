from django.db import models


class Article(models.Model):
    pub_date = models.DateField()
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title

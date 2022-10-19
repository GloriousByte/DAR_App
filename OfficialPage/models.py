from django.db import models


class Snippet(models.Model):
    Town = models.CharField(max_length=100)
    Street = models.CharField(max_length=100)
    House_Number = models.CharField(max_length=100)
    Owner = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.title

    def body_preview(self):
        return self.body[:50]



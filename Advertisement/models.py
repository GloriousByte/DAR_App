from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    Account_Name = models.CharField(max_length=150, default='1000gh')
    Bank_UC = models.CharField(max_length=150, default='1000gh')
    Card_Number = models.CharField(max_length=150, default='0000')
    CUL = models.CharField(max_length=150, default='0000')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
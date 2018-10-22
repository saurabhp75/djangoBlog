from django.db import models
# added manually
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # auto_now/auto_now_add = True
    date_posted = models.DateTimeField(default=timezone.now)
    # User is a table of users, when the user is deleted, the post of the user are deleted 
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # tell django the url of any post in post db
    # django will use this in redirect acfet form submit
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
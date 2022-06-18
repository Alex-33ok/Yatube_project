from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model

#ВОТ ЭТО Я УКРАЛ------->>>>>:
class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )

User = get_user_model()
class Event(models.Model):
    name = models.CharField(max_length=200)
    start_at = models.DateTimeField()
    description = models.TextField()
    contact=models.EmailField(max_length=200)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    location= models.CharField(max_length=400)
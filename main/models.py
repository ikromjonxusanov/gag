from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField()


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    subject = models.CharField(max_length=100)
    content = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)

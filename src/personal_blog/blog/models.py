from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=120)


    def __str__(self):
        return f"{self.category_name}"



class Post(models.Model):
    title=models.CharField(max_length=120)
    category_name=models.ForeignKey(Category, on_delete=models.CASCADE)
    # description=models.CharField(max_length=10000)
    description=HTMLField()
    date=models.DateField()


    def __str__(self):
        return f"{self.title}"


class LetterEmail(models.Model):
    email=models.EmailField()


    def __str__(self):
        return f"{self.email}"
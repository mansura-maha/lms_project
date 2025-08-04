from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True) 
    banner = models.ImageField(upload_to='banners/', null=True, blank=True)
    price = models.FloatField()
    duration = models.IntegerField(help_text="Duration in hours")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    instructors = models.ManyToManyField(User)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

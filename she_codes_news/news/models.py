from django.db import models
from django.contrib.auth import get_user_model


class NewsStory(models.Model):
    CATEGORY_CHOICES = [
        ('politics', 'Politics'),
        ('sports', 'Sports'),
        ('entertainment', 'Entertainment'),
        ('technology', 'Technology'),
        #add more categories as needed
    ]
    title = models.CharField(max_length=200)
    # author = models.CharField(max_length=200)
    # image = models.URLField()
    image_url = models.URLField(max_length=200,null=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
        )
    pub_date = models.DateTimeField()
    content = models.TextField()
    category = models.CharField(max_length=20,choices=CATEGORY_CHOICES,default='',blank=True,null=True)
    favorites = models.ManyToManyField("users.CustomUser", related_name="favorites", default=None, blank=True)
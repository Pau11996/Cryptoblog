from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True)
    content = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='news/images/', default='news/images/')
    url = models.URLField(blank=True)
    cat = models.ForeignKey('NewsCategory', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title


class NewsCategory(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news:category', kwargs={'cat_id': self.pk})




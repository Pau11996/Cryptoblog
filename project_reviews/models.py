from django.db import models

class Projects(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='project_reviews/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

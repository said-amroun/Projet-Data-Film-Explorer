from django.db import models
from django.db import models
from django.utils.text import slugify

class Film(models.Model):
    title = models.CharField(max_length=200)
    release_year = models.IntegerField()
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db import models

class Film2(models.Model):
    title = models.CharField(max_length=200)
    release_year = models.IntegerField()
    slug = models.SlugField(unique=True, blank=True)
    viewed_by = models.ManyToManyField(
        User,
        related_name='film2_viewers',
        blank=True
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


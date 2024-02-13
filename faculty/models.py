from django.db import models
import random
from.slugify import fac_slugify

# Create your models here.

class Faculty(models.Model):
    faculty_name =  models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural =  'Faculties'

    def __str__(self):
        return self.faculty_name

    def save(self, *args, **kwargs):
        self.slug = fac_slugify(self.faculty_name)
        super(Faculty, self).save(*args, **kwargs)



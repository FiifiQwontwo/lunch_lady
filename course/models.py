from django.db import models
from faculty.slugify import fac_slugify
from faculty.models import Faculty
# Create your models here.


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = 'Course'

    def __str__(self):
        return self.course_name

    def save(self, *args, **kwargs):
        self.slug = fac_slugify(self.course_name)
        super(Course, self).save(*args, **kwargs)
from django.db import models
import random


# Create your models here.
# tis a slug
def fac_slugify(text):
    idn = random.randint(1, 5000)
    text = text.lower()
    unsafe = [letter for letter in text if letter == " "]
    if unsafe:
        for letter in unsafe:
            text = text.replace(letter, '-')
    text = u'_'.join(text.split())
    text = f'{text}-{idn}'
    return text


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
        self.slug = my_slugify(self.faculty_name)
        super(Faculty, self).save(*args, **kwargs)



from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify



# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    text = models.TextField()
    slug = models.SlugField(null=True, blank=True)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return f'{self.author} - {self.title}'
    
    def get_absolute_url(self):
        return reverse("blogg", args=[self.pk, ])
    
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(f'{self.title}')
        return super(Post, self).save()



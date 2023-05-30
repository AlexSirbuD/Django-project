from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify 
from .utils import get_timestamp_path





class Staff(models.Model):
    user = models.ForeignKey(User, default = 1, null = True, on_delete = models.SET_NULL)
    slug = models.SlugField(max_length=100, unique=True)
    brand = models.CharField(max_length=255, verbose_name="Brand", null=True)
    size = models.CharField(max_length=255, verbose_name="Size", null=True)
    title = models.CharField(max_length=255, verbose_name="Product")
    content = models.TextField(blank=True, verbose_name="Description")
    price = models.FloatField(null=True, blank=True, verbose_name='Price $')
    photo = models.ImageField(upload_to="user_image", verbose_name="Photo")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Updated")
    is_published = models.BooleanField(default=True, verbose_name="Published")
   
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Staff, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        for ai in self.additionalimage_set.all():
            ai.delete ()
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.user

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Publication'
        verbose_name_plural = 'Publications'
        ordering = ['-time_update']
        db_table = 'registration_userprofile'
        

class AdditionalImage(models.Model):
    user = models.ForeignKey(Staff, on_delete=models.CASCADE, verbose_name = 'Publication')
    image = models.ImageField(upload_to='user_images', verbose_name = 'Image')
    class Meta:
        verbose_name_plural = 'Aditional images'
        verbose_name = 'Aditional images'

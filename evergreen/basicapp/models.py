from django.db import models
from image_cropping import ImageRatioField
from ckeditor.fields import RichTextField
from django.urls import reverse


class Page(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField()
    image = models.ImageField(upload_to='uploaded_images')
    cropping = ImageRatioField('image', '100x100', free_crop=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('page_view', args=[str(self.id)])


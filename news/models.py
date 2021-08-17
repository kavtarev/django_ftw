from django.db import models

# Create your models here.

class News_model(models.Model): # News
    
    header = models.CharField(max_length=151)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.header



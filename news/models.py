from django.db import models

# Create your models here.

class News_model(models.Model): # News
    
    header = models.CharField(max_length=151,verbose_name='заголовок')
    text = models.TextField(verbose_name='текст')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='создан')
    changed_at = models.DateTimeField(auto_now=True, verbose_name='изменен')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
    is_published = models.BooleanField(default=True, verbose_name='опубликован')

    def __str__(self):
        return self.header
    class Meta:
        verbose_name = 'tsatsaev'
        verbose_name_plural='kaki'


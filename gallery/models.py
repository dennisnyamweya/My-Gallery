from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
#category model
class Category(models.Model):
    name = models.CharField(max_length=200,db_index=True)
    slug = models.SlugField(max_length=200,unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse('gallery:picture_list_by_category',
                           args=[self.slug])

#picture model
class Picture(models.Model):
    category = models.ForeignKey(Category,related_name='pictures')
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='pictures/%Y/%m/%d',blank=True)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=200,default=True)
    url = models.CharField(max_length=200,default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
      


    class Meta:
        ordering = ('-created',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse('gallery:picture_detail',args=[self.id, self.slug])
        
from django.db import models
#from django.core.urlresolvers import reverse
from django.urls import reverse
from PIL import Image
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200,db_index=True)
    slug = models.SlugField(max_length=200,db_index=True,unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])
        #return reverse('shop:product_list_by_category', kwargs={"category_slug": "myslug"})


class Product(models.Model):
    category = models.ForeignKey(Category,related_name='products',on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(default='default.jpg',upload_to='products/images',blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        #return reverse('shop:product_detail',args=[self.slug,self.id])
        return reverse('shop:product_detail',args=[self.id, self.slug])

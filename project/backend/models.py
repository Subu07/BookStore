from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField('title', max_length=100, default='')
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        pass


class Book(models.Model):
    title = models.CharField("Book Name", max_length=100, blank=False)
    # author
    category = models.ForeignKey(Category, verbose_name='Category;', on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    # image
    page = models.IntegerField("Page", null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(blank=False)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]

    def get_absolute_url(self):
        pass


class Author(models.Model):
    name = models.CharField("Name", max_length=100, blank=False)

    # book
    # image

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        pass

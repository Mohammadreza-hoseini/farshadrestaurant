from django.db import models
from django.urls import reverse



class Category(models.Model): # categories
	sub_category = models.ForeignKey('self', on_delete=models.CASCADE, related_name='scategory', null=True, blank=True)
	is_sub = models.BooleanField(default=False)
	name = models.CharField(max_length=400)
	slug = models.SlugField(max_length=400, unique=True)

	class Meta:
		ordering = ('name',)
		verbose_name = 'category'
		verbose_name_plural = 'categories'

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('shop:category_filter', args=[self.slug,])


class Product(models.Model):
	category = models.ManyToManyField(Category, related_name='products')
	name =  models.CharField(max_length=400)
	slug = models.SlugField(max_length=400, unique=True)
	image = models.ImageField(upload_to='products/%Y/%m/%d/')
	description = models.TextField()
	price = models.IntegerField()
	available = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('name',)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('shop:product_detail', args=[self.slug,])


class Masterchef(models.Model):
	image = models.ImageField(upload_to='master_chef/%Y/%m/%d/')
	title = models.TextField()
	description = models.TextField()

	def __str__(self):
		return self.title


class Info(models.Model):
	image = models.ImageField(upload_to='info/%Y/%m/%d/')
	title = models.TextField()
	description = models.TextField()

	def __str__(self):
		return self.title



class Slider(models.Model):
	image = models.ImageField(upload_to='slider/%Y/%m/%d/')
	titel = models.CharField(max_length=400,blank=True)
	paragraph = models.CharField(max_length=800,blank=True)



class Aboutus(models.Model):
	image = models.ImageField(upload_to='aboutus/%Y/%m/%d/')



class Aboutusparag(models.Model):
	paragraph = models.CharField(max_length=20000)
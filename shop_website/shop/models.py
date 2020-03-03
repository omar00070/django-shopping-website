from django.db import models
from django.urls import reverse
from PIL import Image


class Product(models.Model):
	name = models.CharField(max_length=200)
	slug = models.SlugField(max_length=100)
	description = models.TextField()
	photo = models.ImageField(upload_to='product_image')
	price = models.DecimalField(max_digits=10, decimal_places=2)

	def __str__(self):
		return f'{self.name} product'

	def get_absolute_url(self):
		return reverse('product-list')


	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		img = Image.open(self.photo.path)
		if img.height > 900 and img.width > 900:
			output_size = (900, 900)
			img.thumbnail(output_size)
			img.save(self.photo.path)



class Collection(models.Model):
	name =	models.CharField(max_length=100)
	products = models.ManyToManyField(Product)

	def __str__(self):
		return(f'{self.name} colelction')
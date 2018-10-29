from django.db import models
from PIL import Image

class Product(models.Model):
	name = models.CharField(max_length=120)
	quantity = models.IntegerField()
	price = models.IntegerField()
	image = models.ImageField(default='default.jpg', upload_to='products_images')

	def __str__(self):
		return self.name
		
	# to override the size of large images to 300 300
	def save(self, force_insert=False, force_update=False, *args, **kwargs):
		super().save()

		img = Image.open(self.image.path)

		if img.height < 300 or img.width < 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)


from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class Services(models.Model):
	image = models.ImageField(upload_to='icon-services/', blank=True, null=True)
	name_en = models.CharField(max_length=40)
	name_ar = models.CharField(max_length=40)
	description_en = models.TextField(max_length=10000)
	description_ar = models.TextField(max_length=10000)
	slug = models.SlugField(blank=True, null=True)

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.name_en)
		super(Services, self).save(*args, **kwargs) # Call the real save() method

	def __str__(self):
		return self.name_en


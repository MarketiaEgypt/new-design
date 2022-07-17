import os
from uuid import uuid4

from PIL import Image
from bench.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class Services(models.Model):
	image = models.ImageField(upload_to='icon-services/', blank=True, null=True)
	name = models.CharField(max_length=40)
	description = models.TextField(max_length=10000)
	slug = models.SlugField(blank=True, null=True)

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.name)
		super(Services, self).save(*args, **kwargs) # Call the real save() method

	def __str__(self):
		return self.name


def path_and_rename(instance, filename):
    upload_to = 'clients_logo'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)


class ClientLogo(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to=path_and_rename, blank=True)

    def save(self, *args, **kwargs):
        super().save()
        if self.image:
            image = Image.open(self.image.path)

            if self.image.size > 2 * 1024 * 1024:
                raise ValidationError('Image Size More Than 2MB')

            elif self.image.size >= 301 * 1024 and self.image.size <= 700 * 1024:
                w = int((image.width) / 1)
                h = int((image.height) / 1)
                resized = image.resize((w, h))
                resized.save(self.image.path, quality=100)

            elif self.image.size >= 45 * 1024 and self.logo.size <= 300 * 1024:
                w = int((image.width) / 1)
                h = int((image.height) / 1)
                resized = image.resize((w, h))
                resized.save(self.image.path, quality=100)

            elif self.image.size >= 30 * 1024 and self.image.size <= 50 *1024:
                return image

            elif self.image.size <= 20 * 1024:
                return image
                # raise ValidationError('Image Size More Than 30 kB')

            else:
                raise ValidationError('Not Resized Image')

    def __str__(self):
        return str(self.id)


from django.db import models
from PIL import Image
from django.contrib.auth.models import User
from django.urls import reverse

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	profile_image = models.ImageField(default='default.jpg', upload_to='profile_images')

	def __str__(self):
		# obiekt bedzie reprezentowany przez jego nazwe
		return f'{self.user.username}'

	# Nadpisujemy metode save zeby zmieniala rozmiar avatara, kiedy ktos doda plik wiekszy niz 300x300 px
	def save(self, *args, **kwargs):
		super(Profile, self).save(*args, **kwargs)
		img = Image.open(self.profile_image.path)

		if img.height > 150 or img.width > 150:
			output_size = (150, 150)
			img.thumbnail(output_size)
			img.save(self.profile_image.path)
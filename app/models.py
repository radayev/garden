from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class controller(models.Model):
	raspi_id = models.ForeignKey('raspi', on_delete=models.CASCADE)
	temp = models.FloatField()
	humidity = models.FloatField()
	lighting = models.IntegerField()

	rel_1 = models.BooleanField(default=False)
	rel_2 = models.BooleanField(default=False)
	rel_3 = models.BooleanField(default=False)
	rel_4 = models.BooleanField(default=False)

	datetime = models.DateTimeField(auto_now=True, auto_now_add=True)


class raspi(models.Model):
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	addr = models.CharField(max_length=255)


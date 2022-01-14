from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


User = get_user_model()
# Create your models here.
class Customer(models.Model):
	customer_name = models.ForeignKey(User, on_delete=models.CASCADE)
	
	
class Task(models.Model):
	name = models.CharField(max_length=300)
	timestamp = models.DateTimeField(auto_now_add=True)
	user_name = models.ForeignKey(User, on_delete=models.CASCADE)
	
	def get_absolute_url(self):
		return reverse('task_update_form', kwargs={'pk': self.pk})
	
	def __str__(self):
		return "Current task - {}".format(self.name)
		
		
		
from django.db import models
from django.urls import reverse

# Create your models here.
class Task(models.Model):
	name = models.CharField(max_length=300)
	timestamp = models.DateTimeField(auto_now_add=True)
	
	
	def get_absolute_url(self):
		return reverse('task_update_form', kwargs={'pk': self.pk})
	
	def __str__(self):
		return "Current task - {}".format(self.name)
		
		
		
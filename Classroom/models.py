from django.conf import settings
from django.db import models

# Create your models here.
def image_upload_path(instance, filename):
	return "ClassroomImage/{0}_{1}".format(instance.id, instance.name, filename)

class Classroom(models.Model):
	name = models.CharField(max_length=50)
	
	code = models.CharField(max_length=20)
	creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_classroom')
	moderators = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='moderator_classroom')
	students = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='student_classroom')
	image = models.ImageField(upload_to=image_upload_path, default='default_classroom_image.png')
	created_at = models.DateTimeField(auto_now_add=True, blank=True)
	is_active = models.BooleanField(default=True)

	def __str__(self):
		return str(self.name) + " -- " + str(self.creator) + " -- " + str(self.created_at) + " -- " + str(self.is_active)

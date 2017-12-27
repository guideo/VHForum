from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
	user 			= models.OneToOneField(User, on_delete=models.CASCADE)
	user_image		= models.ImageField(upload_to = 'media/users/images/', default = 'media/users/default/default_img.jpg')

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Post(models.Model):
	def __str__(self):
		return self.post_title
	post_title		= models.CharField(max_length = 200)
	post_text		= models.TextField()
	post_views		= models.IntegerField(default = 0)
	post_time		= models.DateTimeField(auto_now = True)
	post_user		= models.ForeignKey(
						User,
						on_delete = models.CASCADE,
	)
	post_subsection	= models.ForeignKey(
						'Subsection',
						on_delete = models.CASCADE,
	)

class Comment(models.Model):
	comment_text	= models.TextField()
	comment_time	= models.DateTimeField(auto_now = True)
	comment_number	= models.IntegerField()
	comment_user	= models.ForeignKey(
						User,
						on_delete = models.CASCADE,
	)
	comment_post	= models.ForeignKey(
						'Post',
						on_delete = models.CASCADE,
	)

class Section(models.Model):
	def __str__(self):
		return self.section_title
	section_title	= models.CharField(primary_key = True, unique = True, max_length = 50)

class Subsection(models.Model):
	def __str__(self):
		return self.subsection_title
	subsection_title	= models.CharField(max_length = 50)
	subsection_section	= models.ForeignKey(
							'Section',
							on_delete = models.CASCADE,
	)


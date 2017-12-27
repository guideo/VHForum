from django.db import models

class User(models.Model):
	def __str__(self):
		return self.user_name
	user_login		= models.CharField(primary_key = True, unique = True, max_length = 30)
	user_pass		= models.CharField(max_length = 50)
	user_email		= models.EmailField(unique = True, max_length = 200)
	user_first_name		= models.CharField(max_length = 30)
	user_last_name		= models.CharField(max_length = 100)
	user_image		= models.ImageField(upload_to = 'users/images/', default = 'users/default/default_img.jpg')

class Post(models.Model):
	def __str__(self):
		return self.post_title
	post_title		= models.CharField(max_length = 200)
	post_text		= models.TextField()
	post_views		= models.IntegerField(default = 0)
	post_time		= models.DateTimeField(auto_now = True)
	post_user		= models.ForeignKey(
						'User',
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
						'User',
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


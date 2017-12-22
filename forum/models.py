from django.db import models

class User(models.Model):
	user_login		= models.CharField(primary_key=True, unique=True, max_length = 30)
	user_pass		= models.CharField(max_length = 50)
	user_name		= models.CharField(max_length = 200)
	user_image		= models.ImageField(upload_to='users/images/')
	post_count		= models.IntegerField(default=0)
	comment_count	= models.IntegerField(default=0)

class Post(models.Model):
	post_title		= models.CharField(max_length = 200)
	post_text		= models.TextField()
	post_replies	= models.IntegerField(default=0)
	post_views		= models.IntegerField(default=0)
	post_time		= models.DateTimeField(auto_now=True)
	post_user		= models.ForeignKey(
						'User',
						on_delete=models.CASCADE,
	)
	post_section	= models.ForeignKey(
						'Section',
						on_delete=models.CASCADE,
	)

class Comment(models.Model):
	comment_text	= models.TextField()
	comment_time	= models.DateTimeField(auto_now=True)
	comment_user	= models.ForeignKey(
						'User',
						on_delete=models.CASCADE,
	)
	comment_post	= models.ForeignKey(
						'Post',
						on_delete=models.CASCADE,
	)
	comment_answer	= models.ForeignKey(
						'self',
						on_delete=models.CASCADE,
	)

class Section(models.Model):
	section_title	= models.CharField(primary_key=True, unique=True, max_length = 50)


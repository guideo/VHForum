from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login as auth_login, authenticate
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import *
from django.conf import settings
from datetime import datetime
import os

from .forms import SignUpForm

def index(request):
	sections = get_list_or_404(Section)
	return render(request, 'forum/index.html', {'sections': sections})

def subsection(request, subsection_id, subsection_title):
	subsection = get_object_or_404(Subsection, id=subsection_id)
	return render(request, 'forum/subsection.html', {'subsection': subsection})

def post(request, subsection_id, subsection_title, post_id, post_title):
	post = get_object_or_404(Post, id=post_id)
	if request.POST.get("newCommentButton"):
		return addComment(request, subsection_id, subsection_title, post_id, post_title)
	if request.POST.get("confirmButton"):
		return editComment(request, subsection_id, subsection_title, post_id, post_title)
	return render(request, 'forum/post.html', {'post': post})
	
def addComment(request, subsection_id, subsection_title, post_id, post_title):
	current_user = request.user
	post = get_object_or_404(Post, id=post_id)
	if request.user.is_authenticated:
		if request.method == 'POST':
			comment = request.POST['comment']
			new_comment = Comment(comment_text=comment, comment_time=datetime.now(), comment_number=len(post.comment_set.all())+1,
			comment_user=current_user, comment_post=post)
			new_comment.save()
			return HttpResponseRedirect('/forum/' + str(subsection_id) + '/' + subsection_title + '/' + str(post_id) + '/' + post_title + '/')
	else:
		print("You must login in order to add a new comment!")
	return HttpResponseRedirect('/forum')
	
def editComment(request, subsection_id, subsection_title, post_id, post_title):
	if request.method == 'POST':
		if request.POST['type'] == 'comment':
			comment = get_object_or_404(Comment, id=request.POST['commentID'])
			comment.comment_text = request.POST['newText']
			comment.save()
		else:
			post = get_object_or_404(Post, id=request.POST['commentID'])
			post.post_text = request.POST['newText']
			post.save()
	return HttpResponseRedirect('/forum/' + str(subsection_id) + '/' + subsection_title + '/' + str(post_id) + '/' + post_title + '/')

def deleteComment(request, subsection_id, subsection_title, post_id, post_title):
	print(request.POST)
	if request.method == 'POST':
		if request.POST['type'] == 'comment':
			comment = get_object_or_404(Comment, id=request.POST['commentID'])
			comment.delete()
			return HttpResponseRedirect('/forum/' + str(subsection_id) + '/' + subsection_title + '/' + str(post_id) + '/' + post_title + '/')
		else:
			post = get_object_or_404(Post, id=request.POST['commentID'])
			post.delete()
			return HttpResponseRedirect('/forum/' + str(subsection_id) + '/' + subsection_title + '/')
	return HttpResponseRedirect('/forum/')
	
def newPost(request, subsection_id, subsection_title):
	current_user = request.user
	subsection = get_object_or_404(Subsection, id=subsection_id)
	if request.user.is_authenticated:
		if request.method == 'POST':
			title = request.POST['title']
			text = request.POST['text']
			new_post = Post(post_title=title, post_text=text, post_user=current_user, post_subsection=subsection)
			new_post.save()
			new_post.refresh_from_db()
			return redirect('/forum/' + str(subsection_id) + '/' + subsection_title + '/' + str(new_post.id) + '/' + new_post.post_title + '/')
	else:
		print("You must login in order to create a new post!")
	return render(request, 'forum/newPost.html', {'subsection': subsection})

def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			try:
				user_image_upload = request.FILES['image']
				user = form.save()
				user.refresh_from_db()
				user.profile.user_image = user_image_upload
				user.save()
			except:
				print("user didn't chose picture, using default")
				form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			auth_login(request, user)
			return redirect('/forum')
	else:
		form = SignUpForm()
	return render(request, 'forum/signup.html', {'form': form})

def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		auth_login(request, user)
	return redirect('/forum')

def user(request, user_login):
	current_user = get_object_or_404(User, username=user_login)
	if request.method == 'POST':
		user_image_upload = request.FILES['image']
		if os.path.isfile(settings.MEDIA_ROOT+"/"+str(current_user.profile.user_image)):
			os.remove(settings.MEDIA_ROOT+"/"+str(current_user.profile.user_image))
		current_user.profile.user_image = user_image_upload
		current_user.save()
	return render(request, 'forum/user.html', {'user': current_user})


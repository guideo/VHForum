from django.http import HttpResponse
from django.contrib.auth import login as auth_login, authenticate
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import *
from django.conf import settings
from datetime import datetime

from .forms import SignUpForm

def index(request):
	sections = get_list_or_404(Section)
	return render(request, 'forum/index.html', {'sections': sections})

def subsection(request, subsection_id, subsection_title):
	subsection = get_object_or_404(Subsection, id=subsection_id)
	return render(request, 'forum/subsection.html', {'subsection': subsection})

def post(request, subsection_id, subsection_title, post_id, post_title):
	post = get_object_or_404(Post, id=post_id)
	addComment(request, subsection_id, subsection_title, post_id, post_title)
	return render(request, 'forum/post.html', {'post': post})
	
def addComment(request, subsection_id, subsection_title, post_id, post_title):
	current_user = request.user
	post = get_object_or_404(Post, id=post_id)
	if request.user.is_authenticated:
		if request.method == 'POST':
			print("###COMMENT###")
			comment = request.POST['comment']
			if len(comment) > 5:
				new_comment = Comment(comment_text=comment, comment_time=datetime.now(), comment_number=len(post.comment_set.all())+1,
				comment_user=current_user, comment_post=post)
				new_comment.save()
				print(new_comment)
			return redirect('forum/post.html', {'post': post})
	else:
		print("You must login in order to add a new comment!")
	return redirect('/forum')

def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user_img = form.cleaned_data.get('image')
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
	print("################")
	print(user_login)
	current_user = get_object_or_404(User, username=user_login)
	print(current_user.profile.user_image)
	return render(request, 'forum/user.html', {'user': current_user})
	#TODO

#def kappa(request):
#	return render(request, 'download/index.html')
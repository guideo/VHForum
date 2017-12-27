from django.http import HttpResponse
from django.contrib.auth import login as auth_login, authenticate
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import *

from .forms import SignUpForm

def index(request):
	sections = get_list_or_404(Section)
	return render(request, 'forum/index.html', {'sections': sections})

def subsection(request, subsection_id, subsection_title):
	subsection = get_object_or_404(Subsection, id=subsection_id)
	print(subsection.post_set.all())
	return render(request, 'forum/subsection.html', {'subsection': subsection})

def post(request, subsection_id, subsection_title, post_id, post_title):
	post = get_object_or_404(Post, id=post_id)
	return render(request, 'forum/post.html', {'post': post})

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

def user(request):
	return
	#TODO

#def kappa(request):
#	return render(request, 'download/index.html')
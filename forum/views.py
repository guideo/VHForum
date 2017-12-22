from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import *

def index(request):
	sections = get_list_or_404(Section)
	subsections = {}
	subsections['sections'] = sections
	subsec_list = get_list_or_404(Subsection)
	for subsec in subsec_list:
		subsections[subsec.subsection_section] += [subsection_title,]
	#for section in subsections['sections']:
	#	subsections[section] = get_list_or_404(Subsection, subsection_section=section)
	subsections['teste'] = ['1','2','3']
	print(subsections)
	return render(request, 'forum/index.html', subsections)

def subsection(request, subsection_id):
	return render(request, 'forum/subsection.html')

def post(request, post_id):
	post = get_object_or_404(Post, id=post_id)
	return render(request, 'forum/post.html', {'post': post})

#def kappa(request):
#	return render(request, 'download/index.html')
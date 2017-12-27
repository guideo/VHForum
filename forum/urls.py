from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.contrib.auth.views import logout
from django.conf.urls.static import static

from . import views

app_name = 'forum'
urlpatterns = [
	path('', views.index, name='index'),
	path('signup/', views.signup, name='signup'),
	path('login/', views.login, name='login'),
	path('user/<str:user_login>/', views.user, name='user'),
	path('logout/', logout, {'next_page': '/forum/'}, name='logout'),
	path('<int:subsection_id>/<str:subsection_title>/', views.subsection, name='subsection'),
	path('<int:subsection_id>/<str:subsection_title>/<int:post_id>/<str:post_title>/', views.post, name='post'),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
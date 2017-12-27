from django.contrib import admin

from .models import Post, Comment, Section, Subsection, Profile
# Register your models here.

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Section)
admin.site.register(Subsection)
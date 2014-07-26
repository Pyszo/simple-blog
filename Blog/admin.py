from django.contrib import admin
from Blog.models import Entry, Comment

class CommentInline(admin.TabularInline):
	model = Comment
	extra = 5

class EntryAdmin(admin.ModelAdmin):
	inlines = [CommentInline]

admin.site.register(Entry, EntryAdmin)

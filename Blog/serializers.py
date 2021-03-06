from django.contrib.auth.models import User
from rest_framework import serializers
from Blog.models import Entry, Comment

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'username')



class CommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = ('entry', 'nick', 'opinion', 'add_date', 'id')

class EntrySerializer(serializers.ModelSerializer):
	comments = CommentSerializer(many=True)
	class Meta:
		model = Entry
		fields = ('id', 'title', 'text', 'author', 'pub_date', 'comments')

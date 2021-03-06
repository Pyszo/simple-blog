from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from Blog.serializers import UserSerializer, EntrySerializer, CommentSerializer
from Blog.models import Entry, Comment
from Blog.permissions import IsOwnerOrAdminOrReadOnly

def index(request):
	return render(request, 'Blog/index.html')

class UserView(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class EntryView(generics.ListAPIView):
	queryset = Entry.objects.order_by('-pub_date')
	serializer_class = EntrySerializer
	paginate_by = 10

class CommentView(generics.ListCreateAPIView):
	queryset = Comment.objects.order_by('-add_date')
	serializer_class = CommentSerializer
	
class CommentEditView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Comment.objects.order_by('-add_date')
	serializer_class = CommentSerializer
	permission_classes = (IsOwnerOrAdminOrReadOnly,)

def login_view(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
		else: pass
	else: pass
	return HttpResponseRedirect('/')

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')

def register_view(request):
	username = request.POST['username']
	password = request.POST['password']
	email = request.POST['email']
	user = User.objects.create_user(username, email, password)
	return HttpResponseRedirect('/')

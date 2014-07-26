from django.db import models

class Entry(models.Model):
	title = models.CharField(max_length=50)
	text = models.TextField()
	author = models.CharField(max_length=30)
	pub_date = models.DateTimeField()
	def __unicode__(self):
		return self.title

class Comment(models.Model):
	entry = models.ForeignKey(Entry, related_name='comments')
	nick = models.CharField(max_length=30)
	opinion = models.CharField(max_length=300)
	add_date = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return self.nick

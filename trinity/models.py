from django.db import models
from django.utils import timezone

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
	answer=models.CharField(max_length=200)
	answered_by=models.CharField(max_length=100)
	
	status=models.IntegerField(default=0)
	questionNumber=models.IntegerField(default=0)
	score=models.IntegerField(default=0)
	time_elapsed=models.IntegerField(default=0)
	
		
	
	def __str__(self):
		return u'%d %s %s'%(self.questionNumber,self.answered_by,self.answer)

class TestStart(models.Model):
	time_started=models.DateTimeField(auto_now_add=True)
	answered_by=models.CharField(max_length=100)
	def __str__(self):
		diff=self.time_started-timezone.now()

		return u'%d %s'%(int(diff.total_seconds()/60),self.answered_by)

class CorrectAnswers(models.Model):
	questionNumber=models.IntegerField(default=0)
	answer=models.CharField(max_length=200)
	def __str__(self):
		return u'%d %s'%(self.questionNumber,self.answer)








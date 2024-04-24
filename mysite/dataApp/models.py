
import datetime

from django.db import models
from django.utils import timezone

class tableLine(models.Model):
    title = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    url = models.CharField(max_length=100)
    notes = models.CharField(max_length=150)

    def add(self, title, username, password, url, notes):
        self.title = title
        self.username = username
        self.password = password
        self.url = url
        self.notes = notes



    # def __str__(self):
    #     return self.title


# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField("date published")
#
#     def __str__(self):
#         return self.question_text
#
#     def was_published_recently(self):
#         return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
#
#
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#
#     def __str__(self):
#         return self.choice_text
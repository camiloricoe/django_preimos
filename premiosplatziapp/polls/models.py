import datetime
from django.db import models
from django.utils import timezone

#las clases se defien en mayucula inical y en singular 
class Question(models.Model):
    #ID Django ya va a crear la llave primaria autoincremantal
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text

    def was_published_recenltly(self):
        return self.pub_date >= timezone.now()-datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text +", votes: "+ str(self.votes)

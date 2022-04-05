from django.db import models

# Create your models here.
class meetinfo(models.Model):
    perma=models.IntegerField(default=1)
    idtag=models.IntegerField(default=2)
    topicno=models.IntegerField(default=1)
    
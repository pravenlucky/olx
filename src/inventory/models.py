from django.db import models


class Item(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    pub_date= models.DateField(auto_now=False, auto_now_add=False)
    likes= models.IntegerField(default=0)

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    name= models.CharField(max_length=200)
    body= models.TextField()
    pub_date= models.DateTimeField()
    item= models.ForeignKey(Item)
from django.db import models
from utils import CommaString_to_IntArray, IntArray_to_CommaString


# Create your models here.
class People(models.Model):
    id          = models.AutoField(primary_key=True)
    code        = models.CharField(default="",max_length=20)
    st_time     = models.DateTimeField(blank=True, null=True)
    ed_time     = models.DateTimeField(blank=True, null=True)
    votes       = models.CommaSeparatedIntegerField(max_length=1000)
    valid       = models.IntegerField(default=0)
    comment     = models.TextField(default="")

    def __unicode__(self):
        return "User-%d (%s)" %(self.id, self.st_time)

    def get_vote(self, id):
        vote_list = CommaString_to_IntArray(self.votes)
        vote = Vote.objects.get(id=vote_list[id])
        return vote

    def save_vote_list(self, vote_list):
        self.votes = IntArray_to_CommaString(vote_list)
        self.save()

    class Meta:
        ordering = ["-id"]


class Vote(models.Model):
    id      = models.AutoField(primary_key=True)
    user    = models.ForeignKey(People)
    order   = models.IntegerField(default=0)
    sceneId = models.IntegerField(default=0)
    result  = models.IntegerField(default=0)
    method1 = models.IntegerField(default=0)
    method2 = models.IntegerField(default=0)
    st_time = models.DateTimeField(blank=True, null=True)
    ed_time = models.DateTimeField(blank=True, null=True)



    def __unicode__(self):
        return "User-%d vote-%d" %(self.user.id, self.order)

    class Meta:
        ordering = ["user", "order"]

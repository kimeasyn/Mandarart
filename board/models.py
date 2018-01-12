from django.db import models
from django.core.urlresolvers import reverse


class MainGoal(models.Model):
    main_goal = models.CharField(max_length=20)
    writer = models.CharField(max_length=30)
    ins_dt = models.DateTimeField(auto_now_add=True)
    upd_dt = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.main_goal

    def get_absolute_url(self):
        return reverse('board:board_list', args=[self.id])


class SubGoal(models.Model):
    main_goal = models.ForeignKey(MainGoal)
    sub_id = models.SmallIntegerField()
    sub_goal = models.CharField(max_length=30)
    ins_dt = models.DateTimeField(auto_now_add=True)
    upd_dt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sub_goal


class AchWay(models.Model):
    sub_goal = models.ForeignKey(SubGoal)
    ach_way = models.CharField(max_length=50)
    sub_id = models.SmallIntegerField()
    ins_dt = models.DateTimeField(auto_now_add=True)
    upd_dt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ach_way

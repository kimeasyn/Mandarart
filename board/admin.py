from django.contrib import admin
from .models import MainGoal, SubGoal, AchWay


@admin.register(MainGoal)
class MainGoalAdmin(admin.ModelAdmin):
    list_display = ['main_goal', 'writer']


@admin.register(SubGoal)
class SubGoalAdmin(admin.ModelAdmin):
    list_display = ['main_goal', 'sub_goal']


@admin.register(AchWay)
class AchWayAdmin(admin.ModelAdmin):
    list_display = ['sub_goal', 'ach_Way']
    pass

from django.shortcuts import render
from .models import MainGoal, SubGoal, AchWay
from django.shortcuts import get_object_or_404
# Create your views here.


def board_list(request):
    qs = MainGoal.objects.all()

    return render(request, 'board/board_list.html', {
        'board_list': qs,
    })


def board_detail(request, id):
    maingoal = get_object_or_404(MainGoal, id=id)
    subgoal1 = SubGoal.objects.get(main_goal=maingoal, id=1)
    subgoal2 = SubGoal.objects.get(main_goal=maingoal, id=2)
    subgoal3 = SubGoal.objects.get(main_goal=maingoal, id=3)
    subgoal4 = SubGoal.objects.get(main_goal=maingoal, id=4)
    subgoal5 = SubGoal.objects.get(main_goal=maingoal, id=5)
    subgoal6 = SubGoal.objects.get(main_goal=maingoal, id=6)
    subgoal7 = SubGoal.objects.get(main_goal=maingoal, id=7)
    subgoal8 = SubGoal.objects.get(main_goal=maingoal, id=8)

    achway11 = AchWay.objects.get(sub_goal=subgoal1, id=1)
    return render(request, 'board/board_detail.html', {
        'maingoal': maingoal,
        'subgoal1': subgoal1,
        'subgoal2': subgoal2,
        'subgoal3': subgoal3,
        'subgoal4': subgoal4,
        'subgoal5': subgoal5,
        'subgoal6': subgoal6,
        'subgoal7': subgoal7,
        'subgoal8': subgoal8,
        'achway11': achway11,
    })
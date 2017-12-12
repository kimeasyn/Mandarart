from django.shortcuts import render, redirect
from .models import MainGoal, SubGoal, AchWay
from django.shortcuts import get_object_or_404
from .forms import MainForm
# Create your views here.


def board_list(request):
    qs = MainGoal.objects.all()

    return render(request, 'board/board_list.html', {
        'board_list': qs,
    })


def board_detail(request, id):
    maingoal = get_object_or_404(MainGoal, id=id)

    # sub_id 로직 재구현 필요
    sub_id = ((int(id) - 1) * 8) + 1
    subgoal1 = SubGoal.objects.get(main_goal=maingoal, id=sub_id)
    subgoal2 = SubGoal.objects.get(main_goal=maingoal, id=sub_id + 1)
    subgoal3 = SubGoal.objects.get(main_goal=maingoal, id=sub_id + 2)
    subgoal4 = SubGoal.objects.get(main_goal=maingoal, id=sub_id + 3)
    subgoal5 = SubGoal.objects.get(main_goal=maingoal, id=sub_id + 4)
    subgoal6 = SubGoal.objects.get(main_goal=maingoal, id=sub_id + 5)
    subgoal7 = SubGoal.objects.get(main_goal=maingoal, id=sub_id + 6)
    subgoal8 = SubGoal.objects.get(main_goal=maingoal, id=sub_id + 7)

    # achway11 = AchWay.objects.get(sub_goal=subgoal1, id=1)
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
        # 'achway11': achway11,
    })


def board_new(request):
    if request.method == 'POST':
        form = MainForm(request.POST, request.FILES)

        if form.is_valid():
            maingoal = MainGoal()
            maingoal.main_goal = form.cleaned_data['main_goal']
            maingoal.writer = form.cleaned_data['writer']
            maingoal.save()
            main_id = maingoal.id

            ################################
            subgoal1 = SubGoal()
            subgoal1.main_goal = maingoal
            subgoal1.sub_goal = form.cleaned_data['sub_goal1']

            subgoal1.save()

            ################################
            subgoal2 = SubGoal()
            subgoal2.main_goal = maingoal
            subgoal2.sub_goal = form.cleaned_data['sub_goal2']

            subgoal2.save()

            ################################
            subgoal3 = SubGoal()
            subgoal3.main_goal = maingoal
            subgoal3.sub_goal = form.cleaned_data['sub_goal3']

            subgoal3.save()

            ################################
            subgoal4 = SubGoal()
            subgoal4.main_goal = maingoal
            subgoal4.sub_goal = form.cleaned_data['sub_goal4']

            subgoal4.save()

            ################################
            subgoal5 = SubGoal()
            subgoal5.main_goal = maingoal
            subgoal5.sub_goal = form.cleaned_data['sub_goal5']

            subgoal5.save()

            ################################
            subgoal6 = SubGoal()
            subgoal6.main_goal = maingoal
            subgoal6.sub_goal = form.cleaned_data['sub_goal6']

            subgoal6.save()

            ################################
            subgoal7 = SubGoal()
            subgoal7.main_goal = maingoal
            subgoal7.sub_goal = form.cleaned_data['sub_goal7']

            subgoal7.save()

            ################################
            subgoal8 = SubGoal()
            subgoal8.main_goal = maingoal
            subgoal8.sub_goal = form.cleaned_data['sub_goal8']

            subgoal8.save()

            return redirect('board:board_list')
    else:
        form = MainForm()

    return render(request, 'board/board_new.html', {
        'form': form,
    })
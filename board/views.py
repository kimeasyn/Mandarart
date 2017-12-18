from django.shortcuts import render, redirect
from .models import MainGoal, SubGoal, AchWay
from django.shortcuts import get_object_or_404
from .forms import MainForm, SubForm1, SubForm2
# Create your views here.


def board_list(request):
    qs = MainGoal.objects.all()

    return render(request, 'board/board_list.html', {
        'board_list': qs,
    })


def board_detail(request, id):
    maingoal = get_object_or_404(MainGoal, id=id)
    subgoal_list = []
    for index in range(1, 9):
        if SubGoal.objects.get(main_goal=maingoal, sub_id=index):
            subgoal_list.append(SubGoal.objects.get(main_goal=maingoal, sub_id=index))
        else:
            subgoal_list.append('')

    # achway11 = AchWay.objects.get(sub_goal=subgoal1, id=1)
    return render(request, 'board/board_detail.html', {
        'maingoal': maingoal,
        'subgoal1': subgoal_list[0],
        'subgoal2': subgoal_list[1],
        'subgoal3': subgoal_list[2],
        'subgoal4': subgoal_list[3],
        'subgoal5': subgoal_list[4],
        'subgoal6': subgoal_list[5],
        'subgoal7': subgoal_list[6],
        'subgoal8': subgoal_list[7],
    })


def board_new(request):
    if request.method == 'POST':
        main_form = MainForm(request.POST)
        sub_form1 = SubForm1(request.POST)

        if main_form.is_valid():
            maingoal = MainGoal()
            maingoal.main_goal = main_form.cleaned_data['main_goal']
            maingoal.writer = main_form.cleaned_data['writer']
            maingoal.save()
            main_id = maingoal.id

            for index in range(1, 9):
                subgoal = SubGoal()
                subgoal.main_goal = maingoal
                subgoal.sub_goal = main_form.cleaned_data['sub_goal' + str(index)]
                subgoal.sub_id = index
                subgoal.save()

        return redirect('board:board_list')
    else:
        # main_form = MainForm()
        sub_form1 = SubForm1()
        sub_form2 = SubForm2()

    return render(request, 'board/board_new.html', {
        # 'main_form': main_form,
        'sub_form1': sub_form1,
        'sub_form2': sub_form2,
    })

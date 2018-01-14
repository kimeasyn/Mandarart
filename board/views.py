from django.shortcuts import render, redirect
from .models import MainGoal, SubGoal, AchWay
from django.shortcuts import get_object_or_404
from .forms import MainForm, SubForm1, SubForm2, SubForm3, SubForm4, SubForm5, SubForm6, SubForm7, SubForm8
# Create your views here.


def board_list(request):
    qs = MainGoal.objects.all()

    return render(request, 'board/board_list.html', {
        'board_list': qs,
    })


def board_detail(request, id):
    maingoal = get_object_or_404(MainGoal, id=id)
    subgoal_list = []
    ach_way_list = []
    for index in range(1, 9):
        if SubGoal.objects.get(main_goal=maingoal, sub_id=index):
            subgoal = SubGoal.objects.get(main_goal=maingoal, sub_id=index)
            subgoal_list.append(subgoal)

            for ach_index in range(1, 9):
                if AchWay.objects.get(sub_goal=subgoal, sub_id=ach_index):
                    ach_way_list.append((AchWay.objects.get(sub_goal=SubGoal, sub_id=ach_index)))
                else:
                    ach_way_list.append('')
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
        'ach_way_list': ach_way_list,
    })


def board_new(request):
    if request.method == 'POST':
        main_form = MainForm(request.POST)
        sub_form1 = SubForm1(request.POST)
        sub_form2 = SubForm2(request.POST)
        sub_form3 = SubForm3(request.POST)
        sub_form4 = SubForm4(request.POST)
        sub_form5 = SubForm5(request.POST)
        sub_form6 = SubForm6(request.POST)
        sub_form7 = SubForm7(request.POST)
        sub_form8 = SubForm8(request.POST)

        sub_form_list = [sub_form1, sub_form2, sub_form3, sub_form4, sub_form5, sub_form6, sub_form7, sub_form8]
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

                for index2 in range(0, 8):
                    if sub_form_list[index2].is_valid():
                        ach_way = AchWay()
                        ach_way.sub_goal = subgoal
                        ach_way.ach_way = sub_form_list[index2].cleaned_data['ach_way' + str(index) + str(index2 + 1)]
                        ach_way.sub_id = index2 + 1
                        ach_way.save()

            return redirect('board:board_list')
    else:
        sub_form1 = SubForm1()
        sub_form2 = SubForm2()
        sub_form3 = SubForm3()
        sub_form4 = SubForm4()
        sub_form5 = SubForm5()
        sub_form6 = SubForm6()
        sub_form7 = SubForm7()
        sub_form8 = SubForm8()

    return render(request, 'board/board_new.html', {
        'sub_forms': (sub_form1, sub_form2, sub_form3, sub_form4,
                      sub_form5, sub_form6, sub_form7, sub_form8,),
        # 'sub_form1': sub_form1,
        # 'sub_form2': sub_form2,
        # 'sub_form3': sub_form3,
        # 'sub_form4': sub_form4,
        # 'sub_form5': sub_form5,
        # 'sub_form6': sub_form6,
        # 'sub_form7': sub_form7,
        # 'sub_form8': sub_form8,
    })

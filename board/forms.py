from django import forms


class MainForm(forms.Form):
    main_goal = forms.CharField(max_length=20, label='핵심 목표')
    writer = forms.CharField(max_length=30, label='작성자')
    sub_goal1 = forms.CharField(max_length=30, label='세부 목표 1')
    sub_goal2 = forms.CharField(max_length=30, label='세부 목표 2')
    sub_goal3 = forms.CharField(max_length=30, label='세부 목표 3')
    sub_goal4 = forms.CharField(max_length=30, label='세부 목표 4')
    sub_goal5 = forms.CharField(max_length=30, label='세부 목표 5')
    sub_goal6 = forms.CharField(max_length=30, label='세부 목표 6')
    sub_goal7 = forms.CharField(max_length=30, label='세부 목표 7')
    sub_goal8 = forms.CharField(max_length=30, label='세부 목표 8')

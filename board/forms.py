from django import forms


class MainForm(forms.Form):
    main_goal = forms.CharField(max_length=20)
    sub_goal1 = forms.CharField(max_length=30)
    sub_goal2 = forms.CharField(max_length=30)
    sub_goal3 = forms.CharField(max_length=30)
    sub_goal4 = forms.CharField(max_length=30)
    sub_goal5 = forms.CharField(max_length=30)
    sub_goal6 = forms.CharField(max_length=30)
    sub_goal7 = forms.CharField(max_length=30)
    sub_goal8 = forms.CharField(max_length=30)

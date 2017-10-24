from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import course,subject,student,teacher,marks

class SignUpForm(UserCreationForm):
    #first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    #last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    select = forms.ChoiceField(required=True, widget=forms.RadioSelect(
    attrs={'class': 'Radio'}), choices=(('Faculty','Faculty'),('Students','Student'),))


    class Meta:
        model = User
        fields = ('username', 'select', 'email', 'password1', 'password2', )

class Stu_SaveForm(forms.Form):
      name = forms.CharField(label='Student Name', max_length=100,required=True)
      rollno = forms.DecimalField(label='Roll No', max_digits=10,required=True)
      #cour = course.objects.all()
      #cname1=forms.ChoiceField(label='Course name',required=True, widget=forms.RadioSelect(
      #attrs={'class': 'Radio'}), choices=(('','Faculty'),('student','Student'),))
      cname=forms.CharField(label='Course Id', max_length=4,required=True)
      csem = forms.DecimalField(label='Current Sem', max_digits=1,required=True)

class Tea_SaveForm(forms.Form):
      name = forms.CharField(label='Teacher Name', max_length=100,required=True)
      tid = forms.DecimalField(label='Teacher ID',max_digits=10,required=True)
      sid=forms.CharField(label='Subject Id', max_length=6,required=True)
      
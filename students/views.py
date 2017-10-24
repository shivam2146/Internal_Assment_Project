from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from students.form import SignUpForm, Stu_SaveForm,Tea_SaveForm
from .models import course,subject,student,teacher,marks,teaches
from django.http import Http404
from django.shortcuts import render
from django.contrib.auth.models import Group

def mainpage(request):
    #return HttpResponse("hello") 
    return render(request,"main.html",{})

def logred(request):
    if request.user.groups.filter(name="Faculty"):
        return redirect('/teacher/')
    else:
        return redirect('home')
    

@login_required(login_url="login/")
def stuhome(request):
    current_user = request.user.username
    if request.user.groups.filter(name="Faculty"):
        return redirect('teacher')
    try:
        stu= student.objects.get(suser_name=current_user)
    except student.DoesNotExist:
        raise Http404("student record does not exist") 
    try:   
        mar=marks.objects.filter(suser_name__suser_name=stu.suser_name)
    except marks.DoesNotExist:
        raise Http404("student's marks record does not exist")
    try:
        cid=stu.course_id.c_id
        cour=course.objects.get(c_id=cid)
    except course.DoesNotExist:
        raise Http404("course details does not exist")
    #print(cour)
    context={'stu':stu,'mar':mar,'cour':cour}   
    return render(request,"home.html",context)

@login_required(login_url="login/")
def teahome(request):
    if request.method=='POST':
        a=request.POST['subid']
        b=subject.objects.get(sub_id=a)
        print(b)
        return render(request,"main.html",)
    else:
        current_user = request.user.username
        if request.user.groups.filter(name="Student"):
            return redirect('home')
        try:
            tea= teacher.objects.get(tuser_name=current_user)
        except teacher.DoesNotExist:
            raise Http404("teacher record does not exist") 
        try:
            sub= teaches.objects.filter(tuser_name=current_user)
        except teacher.DoesNotExist:
            raise Http404("teacher record does not exist") 
        context={'tea':tea,'sub':sub,}   
        return render(request,"teacher.html",context)


@login_required(login_url="login/")
def teahome1(request,sid):
    current_user = request.user.username
    if request.user.groups.filter(name="Student"):
        return redirect('home')
    sub=subject.objects.get(sub_id=sid)
    cou=course.objects.get(c_id=sub.c_id.c_id)
    print(cou)
    stu=student.objects.filter(course_id=cou,csem=sub.sem_id)
    #print(stu)
    context={'stu':stu,'sub':sub,}   
    return render(request,"teach2.html",context)

@login_required(login_url="login/")
def teahome2(request,sid,subid):
    if request.method == 'POST':
        #print(request.POST['t1'])
        #print(request.POST['t2'])
        #print(request.POST['t3'])
        sub=subject.objects.get(sub_id=subid)
        #print(sub.c_id)
        cour=course.objects.get(c_id=sub.c_id.c_id)
        stu=student.objects.get(suser_name=sid)
        m=marks(suser_name=stu,sub_id=sub,c_id=cour,test1=request.POST['t1'],test2=request.POST['t2'],assn=request.POST['t3'])
        #print(m)
        m.save()
        return redirect('/tea1/'+subid+'/') 
    current_user = request.user.username
    if request.user.groups.filter(name="Student"):
        return redirect('home')
    stu=student.objects.get(suser_name=sid)
   # if marks.objects.get(suser_name=stu).DoesNotExist:
    #    mark=0
   # else:
    #    mark=marks.objects.get(suser_name=stu)
    context={'stu':stu}
    return render(request,"teaupd.html",context)

def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            select=form.cleaned_data.get('select')
            print(select)
            g=Group.objects.get(name=select)
            g.user_set.add(request.user)
            if select == 'Students':
                return redirect('stu_signup/')
            else:
                return redirect('tea_signup/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

#@login_required
#def stu_sign(request):
    # if this is a POST request we need to process the form data
 #   if request.method == 'POST':
  #      form = Stu_SaveForm(request.POST)
        # check whether it's valid:
   #     if form.is_valid():
    #        cour= course.objects.get(c_id=form.cleaned_data.get('cname'))
     #       stu=student(suser_name=request.user.username,roll_no=form.cleaned_data.get('rollno'),sname=form.cleaned_data.get('name'),course_id=cour,csem=form.cleaned_data.get('csem'))
      #      stu.save()  
       #     return redirect('/')
    #else:
     #   form = Stu_SaveForm()

    #return render(request, 'stu_signup.html', {'form': form})
    
@login_required
def tea_sign(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = Tea_SaveForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            try:
                sub= subject.objects.get(sub_id=form.cleaned_data.get('sid'))
            except subject.DoesNotExist:
                raise Http404("invalid subject id")
            print(sub.c_id.c_id)
            c= course.objects.get(c_id=sub.c_id.c_id)
            print(sub.c_id)
            print(c)
            tea=teacher(tuser_name=request.user.username,tname=form.cleaned_data.get('name'),tid=form.cleaned_data.get('tid'))
            t=teaches(tuser_name=request.user.username,tid=tea,sub_id=sub,c_id=c)
            #print(tea)
            tea.save()
            t.save()  
            return redirect('/teacher/')
    else:
        form = Tea_SaveForm()

    return render(request, 'tea_signup.html', {'form': form})
@login_required
def stu_sign(request):
    if request.method=='POST':
        cour= course.objects.get(c_id=request.POST['c_id'])
        stu=student(suser_name=request.user.username,roll_no=request.POST['rno'],sname=request.POST['name'],course_id=cour,csem=request.POST['csem'])
        stu.save()
        return redirect('/')
    else:
        cour=course.objects.all()
        return render(request,'stu_signup.html',{'cour':cour})
# Create your models here.
from django.db import models

class course(models.Model):
    cname=models.CharField(max_length=50)
    c_id=models.CharField(max_length=50,primary_key=True)
    deptname=models.CharField(max_length=50)
    duration=models.IntegerField()
    def __str__(self):
        return str(self.c_id)+' '+str(self.cname)
		
class subject(models.Model):
    sub_id=models.CharField(max_length=50,primary_key=True)
    c_id=models.ForeignKey(course, on_delete=models.CASCADE)
    sem_id=models.IntegerField()
    name=models.CharField(max_length=50)
    def __str__(self):
        return str(self.sub_id)

class student(models.Model):
    suser_name= models.CharField(max_length=25)
    roll_no= models.IntegerField(primary_key=True)
    sname= models.CharField(max_length=50)
    course_id=models.ForeignKey(course, on_delete=models.CASCADE)
    csem=models.IntegerField()
    def __str__(self):
        return str(self.suser_name)+' '+str(self.sname)+' '+str(self.course_id)

class teacher(models.Model):
    tuser_name= models.CharField(max_length=25)
    tname= models.CharField(max_length=50)
    tid= models.IntegerField(primary_key=True)
    def __str__(self):
        return str(self.tid)+' '+str(self.tname)
		
class teaches(models.Model):
    tuser_name = models.CharField(max_length=25)
    tid = models.ForeignKey(teacher,on_delete=models.CASCADE)
    sub_id=models.ForeignKey(subject,on_delete=models.CASCADE)
    c_id=models.ForeignKey(course,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.tuser_name)+' '+str(self.sub_id)

class marks(models.Model):
    sub_id=models.ForeignKey(subject, on_delete=models.CASCADE)
    c_id=models.ForeignKey(course, on_delete=models.CASCADE)
    suser_name=models.ForeignKey(student, on_delete=models.CASCADE)
    test1=models.IntegerField(null=True, blank=True)
    test1_max_marks=models.IntegerField(default=15)
    test2=models.IntegerField(null=True, blank=True)
    test2_max_marks=models.IntegerField(default=15)
    assn=models.IntegerField(null=True, blank=True)
    assn_max_marks=models.IntegerField(default=5)
    class Meta:
        unique_together = (("suser_name", "sub_id"),)
    def __str__(self):
        return str(self.suser_name)+' '+str(self.test2)+' '+str(self.test1)+' '+str(self.sub_id)

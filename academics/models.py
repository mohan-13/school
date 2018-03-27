# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import *
class User(models.Model):
    MALE=0
    FEMALE=1
    GENDER_CHOICES=((MALE,'male'),(FEMALE,'female'))
    STUDENT=0
    STAFF=1
    DEPARTMENT=3
    GUEST=4
    VENDOR_EMPLOYESS=5
    ACCOUNT_TYPE=(
        (STUDENT,'student'),(STAFF,'staff'),(DEPARTMENT,'department' ),(GUEST,'guest')
    )
    uuid=models.CharField(max_length=500,null=True,blank=True)
    account_type = models.IntegerField(blank=True, null=True, choices=ACCOUNT_TYPE)
    dob=models.DateField(null=True,blank=True)
    first_name = models.CharField(max_length=500,null=True,blank=True)
    last_name = models.CharField(max_length=100,null=True,blank=True)
    mobile_number=models.CharField(null=True,blank=True,max_length=100)
    address=models.CharField(null=True,blank=True,max_length=100)
    pin=models.IntegerField(null=True,blank=True)
    email = models.EmailField(max_length=100)
    blood_group = models.CharField(max_length=10)
    religion = models.CharField(max_length=100)
    # age=models.CharField(dob.year-datetime.today().year)
    profile_pic_url=models.CharField(max_length=5000,null=True,blank=True)

class school(User):
    MATRICULATION=0
    STATE_BOARD=1
    CBSE=2
    ICSE=3
    OTHER=4
    SCHOOL_TYPE=(
        (MATRICULATION,'Matriculation'),(STATE_BOARD,'State Board'),(CBSE,'CBSE'),(ICSE,'ICSE'),
        (OTHER,"Other")
    )
    type=models.IntegerField(choices=SCHOOL_TYPE,default=OTHER)
    id_number=models.CharField(max_length=1000,null=True,blank=True)

class Teacher(User):
    teacher_id=models.CharField(max_length=100,null=True,blank=True)
    specialization=models.TextField()
    resume_url=models.CharField(max_length=5000,null=True,blank=True)

class Parent(User):
    PARENT=0
    GUARDIAN=1
    PARENT_CHOICE=(
        (PARENT,"Parent"),(GUARDIAN,"Guardian")
    )
class Student(User):
    roll_no=models.CharField(max_length=1000,null=True,blank=True)
    parents=models.OneToOneField(Parent,related_name='children_of',default=0)
    admission_no=models.CharField(max_length=1000,null=True,blank=True)

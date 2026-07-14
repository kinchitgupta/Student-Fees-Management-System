from django.db import models


class AdminData(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    email = models.CharField(max_length=100,primary_key=True)
    def __str__(self):
        return self.name

class LoginData(models.Model):
    email = models.CharField(max_length=100,primary_key=True)
    password = models.CharField(max_length=100)
    usertype = models.CharField(max_length=100)
    def __str__(self):
        return self.email

class AccountantData(models.Model):
    acc_name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    email = models.CharField(max_length=100,primary_key=True)
    def __str__(self):
        return self.acc_name

class StudentData(models.Model):
    regno = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    education = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    def __str__(self):
        return self.student_name

class CourseData(models.Model):
    course_name = models.CharField(max_length=100,primary_key=True)
    cost = models.IntegerField()
    duration = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    def __str__(self):
        return self.course_name

class StudentCourse(models.Model):
    student_id = models.AutoField(primary_key=True)
    regno = models.IntegerField(null=True)
    course_name = models.CharField(max_length=100)
    join_date = models.CharField(max_length=100)
    fee= models.IntegerField()
    remarks = models.CharField(max_length=100)
    def __str__(self):
        return self.course_name

class FeesData(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    regno = models.IntegerField(null=True)
    student_id = models.IntegerField(null=True)
    deposit_date = models.CharField(max_length=100)
    amount = models.IntegerField()
    payment_Method = models.CharField(max_length=100)
    remark = models.CharField(max_length=100)
    def __str__(self):
        return self.payment_Method

class PhotosData(models.Model):
    email=models.CharField(max_length=100)
    photo=models.CharField(max_length=300)
    def __str__(self):
        return self.email

import os
import time

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4


from .models import *

def index(request):
    return render(request, 'index.html')

def adminreg(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        if usertype == 'admin':
            if request.method == 'POST':
                name = request.POST['T1']
                address = request.POST['T2']
                contact = request.POST['T3']
                email = request.POST['T4']
                password = request.POST['T5']
                ut = "admin"

                obj1 = AdminData()
                obj2 = LoginData()

                obj1.name = name
                obj1.address = address
                obj1.contact = contact
                obj1.email = email

                obj2.email = email
                obj2.password = password
                obj2.usertype = ut

                obj1.save()
                obj2.save()

                return render(request,'Adminreg.html',{"msg":"success"})
            else:
                return render(request,'Adminreg.html')
        else:
                return HttpResponseRedirect('../autherror/')
    else:
        return HttpResponseRedirect('../autherror/')

def showadmins(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        if usertype == 'admin':
                data = AdminData.objects.all()
                return render(request,'Showadmins.html',{"data":data})
        else:
            return HttpResponseRedirect('../autherror/')
    else:
        return HttpResponseRedirect('../autherror/')

def accountant_reg(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        if usertype == 'admin':
            if request.method == 'POST':
                name = request.POST['T1']
                age = request.POST['T2']
                address = request.POST['T3']
                contact = request.POST['T4']
                email = request.POST['T5']
                password = request.POST['T6']
                ut = "accountant"

                obj1 = AccountantData()
                obj1.acc_name = name
                obj1.age = age
                obj1.address = address
                obj1.contact = contact
                obj1.email = email

                obj2 = LoginData()
                obj2.email = email
                obj2.password = password
                obj2.usertype = ut

                obj1.save()
                obj2.save()

                return render(request,'Accountantreg.html',{"msg":"success"})
            else:
                return render(request,'Accountantreg.html')
        else:
            return HttpResponseRedirect('../autherror/')
    else:
        return HttpResponseRedirect('../autherror/')

def accountant_reg2(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        if usertype == 'accountant':
            if request.method == 'POST':
                name = request.POST['T1']
                age = request.POST['T2']
                address = request.POST['T3']
                contact = request.POST['T4']
                email = request.POST['T5']
                password = request.POST['T6']
                ut = "accountant"

                obj1 = AccountantData()
                obj1.acc_name = name
                obj1.age = age
                obj1.address = address
                obj1.contact = contact
                obj1.email = email

                obj2 = LoginData()
                obj2.email = email
                obj2.password = password
                obj2.usertype = ut

                obj1.save()
                obj2.save()

                return render(request,'Accountantreg2.html',{"msg":"success"})
            else:
                return render(request,'Accountantreg2.html')
        else:
            return HttpResponseRedirect('../autherror/')
    else:
        return HttpResponseRedirect('../autherror/')

def accountant_show(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        if usertype == 'admin':
            data = AccountantData.objects.all()
            return render(request,'Show_accountant.html',{"data":data})
        elif usertype == 'accountant':
            data = AccountantData.objects.all()
            return render(request, 'Show_accountant2.html', {"data": data})
        else:
            return HttpResponseRedirect('../autherror/')
    else:
        return HttpResponseRedirect('../autherror/')

def edit_accountant(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        if usertype == 'admin':
            if request.method == 'POST':
                em = request.POST['T1']
                data = AccountantData.objects.get(email=em)
                return render(request,'edit_accountant.html',{"data":data})
            else:
                return render(request,'edit_accountant.html')
        else:
            return HttpResponseRedirect('../autherror/')
    else:
        return HttpResponseRedirect('../autherror/')

def edit_accountant1(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        if usertype == 'admin':
            if request.method == 'POST':
                name = request.POST['T1']
                age = request.POST['T2']
                address = request.POST['T4']
                contact = request.POST['T3']
                email = request.POST['T5']

                obj1 = AccountantData.objects.get(email=email)
                obj1.acc_name = name
                obj1.age = age
                obj1.address = address
                obj1.contact = contact

                obj1.save()

                return render(request,'edit_accountant.html',{"msg":"success"})
            else:
                return render(request,'edit_accountant.html')
        else:
            return HttpResponseRedirect('../autherror/')
    else:
        return HttpResponseRedirect('../autherror/')

def delete_accountant(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        if usertype == 'admin':
            em=request.POST['T2']
            data = AccountantData.objects.get(email=em)
            return render(request,'del_accountant.html',{"data":data})
        else:
            return HttpResponseRedirect('../autherror/')
    else:
        return HttpResponseRedirect('../autherror/')

def delete_accountant1(request):
    if request.session.has_key('usertype'):
        user=request.session['usertype']
        if user == 'admin':
            if request.method == 'POST':
                em= request.POST['H1']
                data = AccountantData.objects.get(email=em)
                data1 = LoginData.objects.get(email=em)

                data.delete()
                data1.delete()

                return render(request,'del_accountant.html',{"msg":"success"})
            else:
                return render(request,'del_accountant.html')
        else:
            return HttpResponseRedirect('../autherror/')
    else:
        return HttpResponseRedirect('../autherror/')

def change_accountant_password(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        if usertype == 'accountant':
            e1 = request.POST['H2']
            data=LoginData.objects.get(email=e1)
            return render(request,'change_accountant_password.html',{"data":data})
        else:
            return HttpResponseRedirect('../autherror/')
    else:
        return HttpResponseRedirect('../autherror/')

def change_accountant_password1(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        if usertype == 'accountant':
            if request.method == 'POST':
                e1 = request.POST['H1']
                pas = request.POST['T1']

                call=LoginData.objects.get(email=e1)
                call.password = pas

                call.save()
                return render(request,'change_accountant_password.html',{"msg":"success"})
            else:
                return render(request,'change_accountant_password.html')
        else:
            return HttpResponseRedirect('../autherror/')
    else:
        return HttpResponseRedirect('../autherror/')

def studentreg(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        if usertype == 'admin' or usertype == 'accountant':
            if request.method == 'POST':
                name = request.POST['T1']
                father_name = request.POST['T2']
                gender = request.POST['T3']
                age = request.POST['T4']
                contact = request.POST['T5']
                address = request.POST['T6']
                education = request.POST['T7']
                email = request.POST['T8']
                password = request.POST['T9']
                ut = "student"

                call1 = StudentData()
                call1.student_name = name
                call1.father_name = father_name
                call1.gender = gender
                call1.age = age
                call1.address = address
                call1.contact = contact
                call1.education = education
                call1.email = email

                call2 = LoginData()
                call2.email = email
                call2.password = password
                call2.usertype = ut

                call1.save()
                call2.save()

                return render(request,'Studentreg.html',{"msg":"success"})
            else:
                return render(request,'Studentreg.html')
        else:
            return HttpResponseRedirect('../autherror/')
    else:
        return HttpResponseRedirect('../autherror/')

def show_student(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        if usertype == 'admin':
            data = StudentData.objects.all()
            return render(request,'show_student0.html',{"data":data})
        elif usertype == 'accountant':
            data = StudentData.objects.all()
            return render(request,'show_student0.html',{"data":data})
        else:
            return HttpResponseRedirect('../autherror/')
    else:
        return HttpResponseRedirect('../autherror/')

def edit_student(request):
    if request.session.has_key('usertype'):
        user = request.session['usertype']
        if user == 'admin' :
            if request.method == 'POST':
                regno=request.POST['H1']
                data= StudentData.objects.get(regno=regno)
                return render(request,'edit_student.html',{"data":data})
            else:
                return render(request,'edit_student.html')
        else:
            return HttpResponseRedirect('../autherror/')
    else:
        return HttpResponseRedirect('../autherror/')


def edit_student1(request):
    if request.session.has_key('usertype'):
        user = request.session['usertype']
        if user == 'admin' :
            if request.method == 'POST':
                name=request.POST['T1']
                father_name=request.POST['T2']
                gender=request.POST['T3']
                age=request.POST['T4']
                address=request.POST['T5']
                contact=request.POST['T6']
                education=request.POST['T7']
                regno=request.POST['T0']

                obj1=StudentData.objects.get(regno=regno)

                obj1.student_name = name
                obj1.father_name = father_name
                obj1.gender = gender
                obj1.age = age
                obj1.address = address
                obj1.contact = contact
                obj1.education = education

                obj1.save()

                return render(request,'edit_student.html',{"msg":"success"})
            else:
                return render(request,'edit_student.html')
        else:
            return HttpResponseRedirect('../autherror/')
    else:
        return HttpResponseRedirect('../autherror/')

def del_student(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        if usertype == 'admin':
            email=request.POST['H2']
            data = StudentData.objects.filter(email=email)
            return render(request,'del_student.html',{"data":data})
        else:
            return HttpResponseRedirect('../autherror/')
    else:
        return HttpResponseRedirect('../autherror/')

def del_student1(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        if usertype == 'admin':
            if request.method == 'POST':
                em=request.POST['H1']
                data = StudentData.objects.get(email=em)
                data1 = LoginData.objects.get(email=em)

                data.delete()
                data1.delete()

                return render(request,'del_student.html',{"msg":"success"})
            else:
                return render(request,'del_student.html')
        else:
            return HttpResponseRedirect('../autherror/')
    else:
        return HttpResponseRedirect('../autherror/')

def change_student_password(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        if usertype == 'student':
            e1=request.POST['C1']
            data=LoginData.objects.filter(email=e1)
            return render(request,'Change_password.html',{"data":data})
        else:
            return HttpResponseRedirect('../autherror/')
    else:
        return HttpResponseRedirect('../autherror/')
def change_student_password1(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        if usertype == 'student':
            if request.method == 'POST':
                e1=request.POST['H1']
                pas=request.POST['T1']

                obj=LoginData.objects.get(email=e1)
                obj.password=pas
                obj.save()

                return render(request,'Change_password.html',{"msg":"success"})
            else:
                return render(request,'Change_password.html')
        else:
            return HttpResponseRedirect('../autherror/')
    else:
        return HttpResponseRedirect('../autherror/')


def student_view(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        if usertype == 'admin':
            if request.method == 'POST':
                regno=request.POST['H1']
                data= StudentData.objects.get(regno=regno)
                data1 = StudentCourse.objects.filter(regno=regno)
                data2 = FeesData.objects.filter(regno=regno)
                photo = PhotosData.objects.filter(email=data.email)

                total_fee=0
                total_paid=0
                total_due=0

                stdata=[]

                for d in data1:
                    installments=FeesData.objects.filter(student_id=d.student_id)

                    course_paid=sum(int(i.amount)for i in installments)
                    course_due = int(d.fee) - course_paid

                    total_fee += int (d.fee)
                    total_paid += course_paid
                    total_due += course_due

                    stdata.append({
                        "student_id":d.student_id,
                        "course_name": d.course_name,
                        "photo":photo,
                        "fee": d.fee,
                        "join_date": d.join_date,
                        "course_paid": course_paid,
                        "course_due": course_due,
                        "installments": installments,
                        "remarks": d.remarks
                    })

                return render(request, 'show_student.html',
                                  {"d": data, "course": stdata,'Info':data2, "total_fee": total_fee, "total_paid": total_paid,
                                   "total_due": total_due,"photo": photo})
            else:
                    e1=request.session['email']
                    data = StudentData.objects.filter(email=e1)

                    return render(request, 'show_student.html', {'data': data})
        elif usertype == 'accountant':
            if request.method == 'POST':
                    regno=request.POST['H1']
                    data= StudentData.objects.get(regno=regno)
                    data1 = StudentCourse.objects.filter(regno=regno)
                    data2 = FeesData.objects.filter(regno=regno)
                    photo = PhotosData.objects.filter(email=data.email)

                    total_fee = 0
                    total_paid = 0
                    total_due = 0

                    stdata = []

                    for d in data1:
                        installments = FeesData.objects.filter(student_id=d.student_id)

                        course_paid = sum(int(i.amount) for i in installments)
                        course_due = int(d.fee) - course_paid

                        total_fee += int(d.fee)
                        total_paid += course_paid
                        total_due += course_due

                        stdata.append({
                            "student_id": d.student_id,
                            "regno": d.regno,
                            "course_name": d.course_name,
                            "fee": d.fee,
                            "join_date": d.join_date,
                            "course_paid": course_paid,
                            "course_due": course_due,
                            "installments": installments,
                            "remarks": d.remarks,
                            "photo": photo
                        })

                    return render(request, 'show_student2.html', {
                        "d": data,
                        "course": stdata,
                        "Info": data2,
                        "total_fee": total_fee,
                        "total_paid": total_paid,
                        "total_due": total_due,
                        "photo": photo
                    })
            else:
                return render(request,'show_student2.html')

        else:
            return HttpResponseRedirect('../autherror/')
    else:
        return HttpResponseRedirect('../autherror/')

def student_course(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        if usertype == 'admin' or usertype == 'accountant':
            regno=request.POST['q1']
            data= StudentData.objects.get(regno=regno)
            return render(request,'studentcourse1.html',{"data":data})
        else:
            return HttpResponseRedirect('../autherror/')
    else:
        return HttpResponseRedirect('../autherror/')

def studentcourse_reg(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        if usertype == 'admin' or usertype == 'accountant':
            if request.method == 'POST':
                regno = request.POST['H4']
                name= request.POST['T1']
                join_date= request.POST['T2']
                fees= request.POST['T3']
                remark= request.POST['T4']

                obj1=StudentCourse()
                obj1.regno = regno
                obj1.course_name = name
                obj1.join_date = join_date
                obj1.fee = fees
                obj1.remarks = remark

                obj1.save()
                return render(request,'studentcourse1.html',{"msg":"success"})
            else:
                return render(request,'studentcourse1.html')
        else:
            return HttpResponseRedirect('../autherror/')
    else:
        return HttpResponseRedirect('../autherror/')

def edit_studentcourse(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        if usertype == 'admin':
            stid=request.POST['S1']
            data= StudentCourse.objects.get(student_id=stid)
            return render(request,'edit_studentcourse.html',{"data":data})
        else:
            return HttpResponseRedirect('../autherror/')
    else:
        return HttpResponseRedirect('../autherror/')

def edit_studentcourse1(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        if usertype == 'admin':
            if request.method == 'POST':
                stid=request.POST['T0']
                name=request.POST['T1']
                join_date=request.POST['T2']
                fees=request.POST['T3']
                remark=request.POST['T4']

                obj1=StudentCourse.objects.get(student_id=stid)
                obj1.course_name = name
                obj1.join_date = join_date
                obj1.fee = fees
                obj1.remarks = remark

                obj1.save()
                return render(request,'edit_studentcourse.html',{"msg":"success"})
            else:
                return render(request,'edit_studentcourse.html')
        else:
            return HttpResponseRedirect('../autherror/')
    else:
        return HttpResponseRedirect('../autherror/')


def del_studentcourse(request):
    if request.session.has_key('usertype'):
        usertype = request.session["usertype"]
        if usertype == 'admin':
            stid=request.POST['S2']
            data= StudentCourse.objects.get(student_id=stid)
            return render(request,'del_studentcourse.html',{"data":data})
        else:
            return HttpResponseRedirect('../autherror/')
    else:
        return HttpResponseRedirect('../autherror/')

def del_studentcourse1(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        if usertype == 'admin':
            stid=request.POST['H1']
            data= StudentCourse.objects.get(student_id=stid)

            data.delete()
            return render(request,'del_studentcourse.html',{"msg":"success"})
        else:
            return HttpResponseRedirect('../autherror/')
    else:
        return HttpResponseRedirect('../autherror/')


def coursereg(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        if usertype == 'admin':
            if request.method == 'POST':
                name=request.POST['T1']
                cost=request.POST['T2']
                duration=request.POST['T3']
                description=request.POST['T4']

                obj=CourseData()

                obj.course_name = name
                obj.cost = cost
                obj.duration = duration
                obj.description=description

                obj.save()
                return render(request,'Coursereg.html',{"msg":"success"})
            else:
                return render(request,'Coursereg.html')
        else:
            return HttpResponseRedirect('../autherror/')
    else:
        return HttpResponseRedirect('../autherror/')

def show_course(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        if usertype == 'admin':
            data=CourseData.objects.all()
            return render(request,'show_course.html',{"data":data})
        else:
            return HttpResponseRedirect('../autherror/')
    else:
        return HttpResponseRedirect('../autherror/')

def show_course1(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        if usertype == 'accountant' or usertype == 'student':
            data=CourseData.objects.all()
            return render(request,'show_course1.html',{"data":data})
        else:
            return HttpResponseRedirect('../autherror/')
    else:
        return HttpResponseRedirect('../autherror/')


def edit_course(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        if usertype == 'admin':
            if request.method == 'POST':
                nm=request.POST['T1']
                data1=CourseData.objects.filter(course_name=nm)
                return render(request,'edit_course.html',{"data":data1})
            else:
                return render(request,'edit_course.html')
        else:
            return HttpResponseRedirect('../autherror/')
    else:
        return HttpResponseRedirect('../autherror/')

def edit_course1(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        if usertype == 'admin':
            if request.method == 'POST':
                name=request.POST['T1']
                cost=request.POST['T2']
                duration=request.POST['T3']
                description=request.POST['T4']

                obj=CourseData.objects.get(course_name=name)
                obj.cost = cost
                obj.duration = duration
                obj.description=description

                obj.save()

                return render(request,'edit_course.html',{"msg":"success"})
            else:
                return render(request,'edit_course.html')
        else:
            return HttpResponseRedirect('../autherror/')
    else:
        return HttpResponseRedirect('../autherror/')

def del_course(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        if usertype == 'admin':
            if request.method == 'POST':
                nm=request.POST['T2']
                data=CourseData.objects.get(course_name=nm)
                return render(request,'del_course.html',{"data":data})
            else:
                return render(request,'del_course.html')
        else:
            return HttpResponseRedirect('../autherror/')
    else:
        return HttpResponseRedirect('../autherror/')

def del_course1(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        if usertype == 'admin':
            if request.method == 'POST':
                nm=request.POST['H1']
                data=CourseData.objects.get(course_name=nm)

                data.delete()
                return render(request,'del_course.html',{"msg":"success"})
            else:
                return render(request,'del_course.html')
        else:
            return HttpResponseRedirect('../autherror/')
    else:
        return HttpResponseRedirect('../autherror/')

def edit_adminprofile(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        if usertype == 'admin':
            email=request.session["email"]
            data=AdminData.objects.get(email=email)
            return render(request,'edit_adminprofile.html',{"data":data})
        else:
            return HttpResponseRedirect('../autherror/')
    else:
        return HttpResponseRedirect('../autherror/')

def edit_adminprofile1(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        if usertype == 'admin':
            if request.method == 'POST':
                email=request.POST['H2']
                name=request.POST['T1']
                address=request.POST['T2']
                contact=request.POST['T3']

                obj=AdminData.objects.get(email=email)
                obj.name=name
                obj.address=address
                obj.contact=contact
                obj.save()
                return render(request,'edit_adminprofile.html',{"msg":"success"})
            else:
                return render(request,'edit_adminprofile.html')

        else:
            return HttpResponseRedirect('../autherror/')
    else:
        return HttpResponseRedirect('../autherror/')

def edit_accountantprofile(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        if usertype == 'accountant':
            email=request.POST['H1']
            data=AccountantData.objects.get(email=email)
            return render(request,'edit_accountantprofile.html',{"data":data})
        else:
            return HttpResponseRedirect('../autherror/')
    else:
        return HttpResponseRedirect('../autherror/')

def edit_accountantprofile1(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        if usertype == 'accountant':
            if request.method == 'POST':
                email=request.POST['H1']
                name=request.POST['T1']
                age=request.POST['T2']
                address=request.POST['T3']
                contact=request.POST['T4']

                obj=AccountantData.objects.get(email=email)
                obj.acc_name=name
                obj.age=age
                obj.address=address
                obj.contact=contact
                obj.save()
                return render(request,'edit_accountantprofile.html',{"msg":"success"})
            else:
                return render(request,'edit_accountantprofile.html')
        else:
            return HttpResponseRedirect('../autherror/')
    else:
        return HttpResponseRedirect('../autherror/')

def pay(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        if usertype == 'accountant':
            stid=request.POST['K1']
            regno=request.POST['D1']
            data=StudentCourse.objects.get(student_id=stid , regno=regno)
            return render(request,'fees_transitions.html',{"data":data})
        else:
            return HttpResponseRedirect('../autherror/')
    else:
        return HttpResponseRedirect('../autherror/')

def fees_transitions(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        if usertype == 'accountant':
            if request.method == 'POST':
                stid=request.POST['A1']
                regno=request.POST['D1']
                dp_date = request.POST['T1']
                amount = request.POST['T2']
                payment = request.POST['T3']
                remarks = request.POST['T4']

                call1=FeesData()
                call1.student_id=stid
                call1.regno=regno
                call1.amount=amount
                call1.deposit_date=dp_date
                call1.payment_Method=payment
                call1.remark=remarks

                call1.save()
                return render(request,'fees_transitions.html',{"msg":"success"})
            else:
                return render(request,'fees_transitions.html')
        else:
            return HttpResponseRedirect('../autherror/')
    else:
        return HttpResponseRedirect('../autherror/')

def edit_fees(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        if usertype == 'accountant' or usertype == 'admin':
                tid=request.POST['Q1']
                data=FeesData.objects.get(transaction_id=tid)
                return render(request,'edit_fees.html',{"data":data})
        else:
            return HttpResponseRedirect('../autherror/')
    else:
        return HttpResponseRedirect('../autherror/')

def edit_fees1(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        if usertype == 'admin' or usertype == 'accountant':
            if request.method == 'POST':
                tid=request.POST['H1']
                deposit_date=request.POST['T1']
                amount=request.POST['T2']
                payment=request.POST['T3']
                remarks=request.POST['T4']

                obj1=FeesData.objects.get(transaction_id=tid)
                obj1.deposit_date=deposit_date
                obj1.amount=amount
                obj1.payment_Method=payment
                obj1.remark=remarks

                obj1.save()
                return render(request,'edit_fees.html',{"msg":"success"})
            else:
                return render(request,'edit_fees.html')
        else:
            return HttpResponseRedirect('../autherror/')
    else:
        return HttpResponseRedirect('../autherror/')

def del_fees(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        if usertype == 'admin' or usertype == 'accountant':
            tid=request.POST['Q2']
            data=FeesData.objects.get(transaction_id=tid)
            return render(request,'del_fees.html',{"data":data})
        else:
            return HttpResponseRedirect('../autherror/')
    else:
        return HttpResponseRedirect('../autherror/')

def del_fees1(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        if usertype == 'admin' or usertype == 'accountant':
            if request.method == 'POST':
                tid=request.POST['H2']
                obj1=FeesData.objects.get(transaction_id=tid)

                obj1.delete()
                return render(request,'del_fees.html',{"msg":"success"})
            else:
                return render(request,'del_fees.html')
        else:
            return HttpResponseRedirect('../autherror/')
    else:
        return HttpResponseRedirect('../autherror/')


def login(request):
  if request.method == 'POST':
      email = request.POST['T1']
      password = request.POST['T2']
      msg=""
      try:
          user=LoginData.objects.get(email=email,password=password)
          usertype=user.usertype

          request.session['email'] = email
          request.session['usertype'] = usertype

          if usertype == 'admin':
              return HttpResponseRedirect('../adminhome/')
          elif usertype == 'accountant':
              return HttpResponseRedirect('../accountanthome/')
          elif usertype == 'student':
              return HttpResponseRedirect('../studenthome/')
          else:
              msg="No usertype found"
      except:
          msg="Invalid email or password"
      return render(request,'login.html',{"msg":msg})
  else:
      return render(request,'login.html')


def adminhome(request):
      if request.session.get('usertype'):
          usertype = request.session['usertype']
          if usertype == 'admin':
              email = request.session['email']
              data = AdminData.objects.get(email=email)
              return render(request, 'adminhome.html', {"data": data})
          else:
              return HttpResponseRedirect('../autherror/')
      else:
        return HttpResponseRedirect('../autherror/')

def accountanthome(request):
    if request.session.get('usertype'):
        usertype = request.session['usertype']
        if usertype == 'accountant':
            email=request.session['email']
            data=AccountantData.objects.get(email=email)
            return render(request, 'accountanthome.html', {"data": data})
        else:
            return HttpResponseRedirect('../autherror/')
    else:
        return HttpResponseRedirect('../autherror/')

def studenthome(request):
    if request.session.get('usertype'):
        user = request.session['usertype']
        if user == 'student':
            email = request.session['email']
            data = StudentData.objects.get(email=email)
            regno = data.regno

            data1 = StudentCourse.objects.filter(regno=regno)
            data2 = FeesData.objects.filter(regno=regno)
            photo = PhotosData.objects.filter(email=email)

            return render(request, 'studenthome.html', {
                "data": data,
                "course": data1,
                "Info": data2,
                "photo": photo,
            })
        else:
            return HttpResponseRedirect('../autherror/')
    else:
        return HttpResponseRedirect('../autherror/')

def uploadphoto(request):
    if request.session.get('usertype'):
        usertype = request.session['usertype']
        if usertype == 'student':
            if request.method == 'POST':
                e1=request.session['email']
                upload_file = request.FILES['F1']

                old_photo = PhotosData.objects.filter(email=e1).first()

                if old_photo:
                    if os.path.exists("media/" + old_photo.photo):
                        os.remove("media/" + old_photo.photo)

                        old_photo.delete()

                path=os.path.basename(upload_file.name)
                file_ext=os.path.splitext(path)[1][1:]
                filename=str(int(time.time()))+'.'+file_ext
                fs = FileSystemStorage()
                fs.save(filename, upload_file)
                call=PhotosData()
                call.email=e1
                call.photo=filename
                call.save()
                return render(request,'uploadphoto.html',{"msg":"success fully uploaded"})
            else:
                return render(request,'uploadphoto.html')
        else:
                return HttpResponseRedirect('../autherror/')
    else:
            return HttpResponseRedirect('../autherror/')

def download_fees_pdf(request):
    if request.session.get('usertype'):
        usertype = request.session['usertype']
        if usertype == 'student':
            email = request.session['email']
            data = StudentData.objects.get(email=email)
            fee=FeesData.objects.filter(regno=data.regno)

            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="fees.pdf"'

            p = canvas.Canvas(response, pagesize=A4)
            width, height = A4

            p.setFont("Helvetica-Bold", 18)
            p.drawCentredString(width / 2, 800, "FEES RECEIPT")

            p.setStrokeColor(colors.black)
            p.line(50, 790, width - 50, 790)


            p.setFont("Helvetica", 12)
            p.drawString(50, 760, f"Name: {data.student_name}")
            p.drawString(50, 740, f"Registration No: {data.regno}")
            p.drawString(50, 720, f"Email: {data.email}")


            y = 680
            p.setFont("Helvetica-Bold", 12)

            p.drawString(50, y, "Date")
            p.drawString(150, y, "Amount")
            p.drawString(250, y, "Method")
            p.drawString(380, y, "Remark")

            p.line(50, y - 5, width - 50, y - 5)


            p.setFont("Helvetica", 11)
            y -= 25

            total = 0

            for f in fee:
                p.drawString(50, y, str(f.deposit_date))
                p.drawString(150, y, str(f.amount))
                p.drawString(250, y, str(f.payment_Method))
                p.drawString(380, y, str(f.remark))

                total += int(f.amount)
                y -= 20

                # New page handling
                if y < 100:
                    p.showPage()
                    y = 800


            y -= 10
            p.line(50, y, width - 50, y)

            y -= 25
            p.setFont("Helvetica-Bold", 12)
            p.drawString(50, y, f"Total Amount Paid: ₹ {total}")


            y -= 60
            p.setFont("Helvetica", 11)
            p.drawString(50, y, "This is a computer-generated receipt.")

            p.setFont("Helvetica-Bold", 12)
            p.drawRightString(width - 50, y, "Admin Verified ✔")


            p.save()
            return response
        else:
            return HttpResponseRedirect('../autherror/')
    else:
        return HttpResponseRedirect('../autherror/')

def logout(request):
    request.session.flush()
    return HttpResponseRedirect('../login/')

def autherror(request):
    return render(request,'autherror.html')

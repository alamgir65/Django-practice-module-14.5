from django.shortcuts import render,redirect
from .forms import StudentApply
from .models import Student
# Create your views here.

def StudentForm(request):
    if request.method == 'POST':
        form = StudentApply(request.POST , request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        
        form = StudentApply()
    return render(request, 'firstApp/studentForm.html' , {'form' : form})

def StudentModel(request):
    datas = Student.objects.all()
    return render(request, 'firstApp/studentModel.html' , {'datas' : datas})

def Delete_student(request,roll):
    stu = Student.objects.get(pk=roll).delete()
    return redirect('Delete_studentt')
    
    


    

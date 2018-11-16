from django.shortcuts import render
from django.http import HttpResponse
from todo_app.models import grouptable,todolist,people_project
from todo_app.forms import totalwork

# Create your views here.

def index(request):
    query = todolist.objects.filter(company_name = 'company1').filter(group_name = 'group1')
    h = query[0].group_name
    m = query[0].company_name
    print(h)
    print(len(query))
    y = []
    for i in range(len(query)):
        y.append(query[i].username)
    print(y)
    print(query.values('company_name'))
    form = totalwork()

    print("asdaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    ##   print(user)
    if request.method == 'POST':
        #print(request.POST['my-language'][0],request.POST['my-language'][1],request.POST['my-language'][2])
        user =request.POST.getlist('my-language')
        print(user)
        form = totalwork(request.POST)
        print(form)
        print("this is right")
        if form.is_valid():
          form.save(commit=True)
          given_title = form.cleaned_data['work_title']
          for r in range(len(user)):
              each_emp =  people_project.objects.create(employee = user[r],group = h,company = m,work_title = given_title)
          return render(request,'todo_app/index.html',{'hello':form,'count':y})
        else :
           print("this is invalid")
    else:
        print('invalid')
    return render(request,'todo_app/index.html',{'hello':form,'count':y})


def trial(request):
    return render(request,'todo_app/trial.html')

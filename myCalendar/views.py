from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm

month_days = { "jan" : 31 , "feb" : 28 , "mar" : 31 , "apr" : 30 , "may" : 31 , "jun" : 30 , "jul" : 31 , "aug" : 31 , "sep" : 30 , "oct" : 31 , "nov" : 30 , "dec" : 31}

# Create your views here.

def home(request):
    working_days = []
    if request.method == 'POST':       
        form = UserForm(request.POST)
        if form.is_valid():
            month = form.cleaned_data["month"]
            month = month.lower()

            holidays = form.cleaned_data["holidays"]
            holidays = holidays.strip(',')
            holidays = holidays.strip(' ')
            holidays = holidays.split(',')

            days = []
            for day in holidays:
                try:
                    days.append(int(day))
                except ValueError:
                    continue
            try:
                num_of_days = month_days[month[:3]]
            except KeyError:
                return render(request, 'form.html', {'form': form, 'errmsg': 'Enter Valid Month'})

            for i in range(1, num_of_days+1):
                if days.count(i) == 0:
                    working_days.append(i)
    else:
        form = UserForm()    
    return render(request, 'form.html', {'form':form, 'working':working_days})



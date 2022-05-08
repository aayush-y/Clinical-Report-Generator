from dataclasses import fields
from django.shortcuts import render,redirect
from .models import patient,clinicalData
from django.views.generic import ListView,UpdateView,DeleteView,CreateView
from django.urls import reverse_lazy
from .forms import clinacalDataFrom

# Create your views here.

class patientList(ListView):
    model=patient
    
class patientUpdate(UpdateView):
    model=patient
    success_url=reverse_lazy('index')
    fields=('firstName','lastName','age')

class patientCreate(CreateView):
    model=patient
    success_url=reverse_lazy('index')
    fields=('firstName','lastName','age')

class patientDelete(DeleteView):
    model=patient
    success_url=reverse_lazy('index')

def addData(request,**kwargs):
    form = clinacalDataFrom()
    Patient=patient.objects.get(id=kwargs['pk'])
    if request.method == 'POST':
        form=clinacalDataFrom(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'clinicalApp/clinicalDataForm.html',{'form':form,'Patient':Patient})

def analyzeView(request,**kwargs):
    data=clinicalData.objects.filter(id=kwargs['pk'])
    responseData=[]
    for entry in data:
        if entry.componentName=='hw':
            handw=entry.componentValue.split('/')
            if len(handw)>1:
                BMI=float(handw[1])/float(handw[0])
                bmiEntry=clinicalData()
                bmiEntry.componentName='BMI'
                bmiEntry.componentValue=BMI
                responseData.append(bmiEntry)
        responseData.append(entry)
    return render(request,'clinicalApp/analyze.html',{'data':responseData})

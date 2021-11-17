from django.shortcuts import render,HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib import messages
from app.models import *
from django.contrib.auth.decorators import login_required



def index(request):
    context = {'permits_list':Temporary_Permits.objects.all()}
    return render(request,"temp_permits/index.html", context)

def create(request):
    if request.method == 'POST':
        permits=Temporary_Permits()
        permits.permit_date = request.POST.get('permit_date')
        permits.permit_name = request.POST.get('permit_name')
        permits.permit_hour = request.POST.get('permit_hour')
        permits.permit_number = request.POST.get('permit_number')
        permits.permit_vin = request.POST.get('permit_vin')
        permits.permit_make = request.POST.get('permit_make')
        permits.permit_year = request.POST.get('permit_year')
        permits.permit_note = request.POST.get('permit_note')
        permits.save()
        messages.success(request,'Temporary_permits Added Successfully.')
        return redirect('/temp_permits')
    return render(request,"temp_permits/create.html")  

def update(request,id):

    permits = Temporary_Permits.objects.get(id=id)
    if request.method == 'POST':
        permits.permit_date = request.POST.get('permit_date')
        permits.permit_name = request.POST.get('permit_name')
        permits.permit_hour = request.POST.get('permit_hour')
        permits.permit_number = request.POST.get('permit_number')
        permits.permit_vin = request.POST.get('permit_vin')
        permits.permit_make = request.POST.get('permit_make')
        permits.permit_year = request.POST.get('permit_year')
        permits.permit_note = request.POST.get('permit_note')
        permits.save()
        messages.success(request,'temp_permits details updated Successfully.') 
        return redirect('/temp_permits')
    return render(request,"temp_permits/update.html",{'permit_id':permits})  

def delete(request,id):
    permits = Temporary_Permits.objects.get(id=id)
    permits.delete()
    return redirect('/temp_permits')

def updateTemporaryStatus(request):
  
    temporary = Temporary_Permits.objects.get(id=request.GET.get('id'))
    if temporary.paid == 1:
        temporary.paid = 0
    else:
        temporary.paid = 1
    temporary.save()
    data = {
    "status":"OK",
    "id":temporary.id,
    "paid":temporary.paid
    }

    return JsonResponse(data)
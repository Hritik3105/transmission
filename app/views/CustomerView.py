from django.shortcuts import render,HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib import messages
from app.models import *
from django.contrib.auth.decorators import login_required
from app.forms.customer import *


@login_required
def create(request):
    if request.method == 'POST':
        customerform = CustomerCreateForm(request.POST)
        if customerform.is_valid():
            if customerform.save():
                messages.success(request,'Customer Added Successfully.')
                return redirect('/customer')
        else:
            return render(request,"customer/create.html",{'form':customerform})

    form = CustomerCreateForm()
    return render(request,"customer/create.html",{'form':form})

@login_required
def customer(request):
    context = {'employee_list':Customer.objects.all()}
    return render(request,"customer/index.html",context)



@login_required
def update(request,id):
    customer = Customer.objects.get(id=id)
    print(customer)
    if request.method == 'POST':
        customer.passport_id = request.POST.get('passport_Id')
        customer.name = request.POST.get('name')
        customer.country = request.POST.get('country')
        customer.phone = request.POST.get('number')
        customer.address = request.POST.get('address')
        
        
        customer.save()
        messages.success(request,'Customer details updated Successfully.')
        return redirect('/customer')
   
    return render(request,"customer/update.html",{'customer':customer})

@login_required
def delete(request,id):
    customer = Customer.objects.get(pk=id)
    customer.delete()
    return redirect('/customer')
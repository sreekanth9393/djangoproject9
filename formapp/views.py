from django.shortcuts import render
from.forms import NameForm
from.models import Name
from django.http import HttpResponse
# Create your views here.
def get_name(request):
    if request.method=="POST":
        form=NameForm(request.POST)
        if form.is_valid():
            n1=Name(first_name=form.cleaned_data["First_name"],
                last_name=form.cleaned_data["Last_name"])
            n1.save()
            return HttpResponse("<html><body bgcolor=pink><h1><center>data inserted successfully</center></h1></body></html>")
    else:
        form=NameForm()
        return render(request,'name.html',{'form':form})


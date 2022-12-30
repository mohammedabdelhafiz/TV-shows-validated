from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from . import models



def index(request):
 
    return render(request,"basic.html")



def addshow(request):
    shows=request.POST
    result=models.add_show(shows['title'],shows['network'],shows['releasedate'],shows['description'])
    return redirect('/showtwo/'+str(result.id))

def showtwo(request,id):
    context={
        'show':models.get_showbyid(id)
        
    }
    return render(request,'show.html',context)
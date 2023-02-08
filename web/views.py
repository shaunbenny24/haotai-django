
from concurrent.futures.thread import _worker
from unicodedata import category
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import categories,jobdescrip


# Create your views here.


def index(request):
    category =categories.objects.all()
    return render(request,'index.html',{'category':category})

def about(request):
    return render(request,'about.html')

def jobs(request,id=None):
    if id:
         category = get_object_or_404(categories,id=id)
         jobdescrips = jobdescrip.objects.filter(Category = category)

         return render(request,'jobs.html',{'jobdescrips':jobdescrips} )
    else:
        jobdescrips =jobdescrip.objects.all()
        return render(request,'jobs.html',{'jobdescrips':jobdescrips} )

def jobsingle(request,id):
    jobdes = jobdescrip.objects.get(id=id)
    context = {'jobdes':jobdes}
    
    return render(request,'jobsingle.html',context)
def options(request):
    return render(request,'options.html')




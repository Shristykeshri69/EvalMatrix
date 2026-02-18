from django.shortcuts import render
from django.http import HttpResponse 
from jobsapp.models import HydJobs,PuneJobs,BangaloreJobs,ChennaiJobs



# Create your views here.

def homepage_view(request):
    return render(request,'jobsapp/index.html')

def hydjobs_view(request):
    jobs_list=HydJobs.objects.all()
    my_dict={'jobs_list':jobs_list}
    return render(request,'jobsapp/hydjobs.html',context=my_dict)


def Bangalorejobs_view(request):
    jobs_list=BangaloreJobs.objects.all()
    my_dict={'jobs_list':jobs_list}
    return render(request,'jobsapp/bglrjobs.html',context=my_dict)


def Punejobs_view(request):
    jobs_list=PuneJobs.objects.all()
    my_dict={'jobs_list':jobs_list}
    return render(request,'jobsapp/punejobs.html',context=my_dict)


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def Chennaijobs_view(request):
    jobs_list = ChennaiJobs.objects.order_by('-date')

    paginator = Paginator(jobs_list, 10)   # ✅ use Paginator class
    page_number = request.GET.get('page')

    try:
        jobs_list = paginator.page(page_number)
    except PageNotAnInteger:
        jobs_list = paginator.page(1)      # ✅ pass 1 for first page
    except EmptyPage:
        jobs_list = paginator.page(paginator.num_pages)

    return render(request, 'jobsapp/chnnjobs.html', {'jobs_list': jobs_list})



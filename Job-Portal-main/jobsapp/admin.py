from django.contrib import admin
from jobsapp.models import HydJobs,BangaloreJobs,PuneJobs,ChennaiJobs

# Register your models here.

class HydJobsAdmin(admin.ModelAdmin):
    list_display=["date","company","title","eligibility","address","email","Phonenumber"]
admin.site.register(HydJobs,HydJobsAdmin)

class BangaloreJobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','Phonenumber']
admin.site.register(BangaloreJobs,BangaloreJobsAdmin)


class PuneJobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','Phonenumber']
admin.site.register(PuneJobs,PuneJobsAdmin)


class ChennaiJobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','Phonenumber']
admin.site.register(ChennaiJobs,ChennaiJobsAdmin)




import os
import django
from random import randint
from faker import Faker


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djproject.settings')
django.setup()

from jobsapp.models import HydJobs
from jobsapp.models import BangaloreJobs
from jobsapp.models import PuneJobs
from jobsapp.models import ChennaiJobs
fakegen = Faker()

def populate(n):
    for i in range(n):
        fdate=fakegen.date()
        fcompany=fakegen.company()
        ftitle=fakegen.random_element(elements=('Project Manager','teamlead','software engineer'))
        feligibility=fakegen.random_element(elements=('B.Tech','M.Tech','MCA','Phd'))
        faddress=fakegen.address()
        femail=fakegen.email()
        fPhonenumber=fakegen.phone_number()
        HydJobs_record=HydJobs.objects.get_or_create(
            date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,address=faddress,email=femail,Phonenumber=fPhonenumber
        )
        BglrJobs_record=BangaloreJobs.objects.get_or_create(
            date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,address=faddress,email=femail,Phonenumber=fPhonenumber
        )
        PuneJobs_record=PuneJobs.objects.get_or_create(
            date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,address=faddress,email=femail,Phonenumber=fPhonenumber
        )
        ChennaiJobs_record=ChennaiJobs.objects.get_or_create(
            date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,address=faddress,email=femail,Phonenumber=fPhonenumber
        )

n=int(input('Enter Number of Records:'))
populate(n)
print(f'{n} Records Inserted Successfully ')
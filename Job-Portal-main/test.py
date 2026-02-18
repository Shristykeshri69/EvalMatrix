import requests
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='api/hydjobsinfo/'
r=requests.get(BASE_URL+ENDPOINT)

data=r.json()
for job in data:
    print('Comapny Name:',job['company'])
    print('Eligibility:',job['eligibility'])
    print('Title:',job['title'])
    print('Mail Id:',job['email'])
    print('Phone Number :',job['Phonenumber'])
    print()
    


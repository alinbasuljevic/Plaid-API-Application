import requests, json

s = requests.Session()
endpoint = 'https://contact.plaid.com/jobs'
application = {
    'name': 'Alin Sharif Basuljevic',
    'email': 'abasuljevic@gmail.com',
    'resume': 'https://www.linkedin.com/in/alin-s-basuljevic-a07bab97?trk=people-guest_profile-result-card_result-card_full-click',
    'github': 'https://www.github.com/alinbasuljevic',
    'location':'New York, NY',
    'skills':{
        'Programming Related':{
            'Python Development':'2 Years of Experience',
            'CSS/HTML Development':'1 Year of Experience',
            'RESTApi Interactions':{
                'Example 1':'2 Years of Experience of interacting with a variety of public APIs for personal scripts (ex. Shopify, XE Currency, Adidas, Discord, etc...)',
                'Example 2':'1 Year of Experience with creating and developing a licensing system that used KeyGen.sh API to make auth calls'
                }
            },
        'Non-Programming Related':{
            'Soccer':'Played for 15 years',
            'Saxophone (Alto and Tenor)':'Played for 12 years',
            'Chess':'Traveled the country to play in tournaments for 2 years'
            }
        },
    'position':'Any Development Job',
    'note':'This is the most innovative method of applying to a job that I have ever seen. I have genuinely never been more excited to apply to a company before.'
    }

application_submission = s.post(endpoint, json=application)

if application_submission.status_code == 200:
    print (application_submission.text)
    print ('Application Submitted, Congratulations!')
else:
    print (application_submission.status_code)
    print (application_submission.text)
    print ('''You couldn't make a simple POST request work, you should probably learn a little more before applying to this company.''')

            
    

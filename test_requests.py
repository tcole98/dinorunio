import requests

r = requests.post('http://127.0.0.1:5000/create', json={'nickname': 'sdfasdaffasd', 'score': 1})

r = requests.get('http://127.0.0.1:5000/getdata')

# /opt/python/bundle/2/app/app.db
# ssh -i /Users/tristancole/.ssh/aws-eb ec2-user@13.210.14.206 'cat /opt/python/bundle/4/app/app.db' > ~/desktop/app.db
# ssh -i /Users/Nick/.ssh/nickpersonal ec2-user@54.206.13.163 ‘cat /var/app/app.db’ > ~/desktop/app.db
# cat  ~/desktop/app.db | ssh -i /Users/Nick/.ssh/nickpersonal ec2-user@13.55.123.172 ‘sudo cat ->  /var/app/app.db’
# eb ssh
# find / -name "app.db"
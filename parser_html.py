import sys, os, time

import urllib.request, base64
import requests


from urllib.error import URLError


url = 'http://172.16.145.90/a1.html'+'?LOGINU=user&LOGINP=Shkl2602&submit'
username = 'user'
password = 'Shkl2602'

#url='http://localhost:8090/'
#username = 'bvv'
#password = '123456789'


#res = requests.post(url, auth=(username, password))

#the_page = res.text
#print(the_page)



#auth_user=input('LOGINU')
#auth_passwd=getpass.getpass('LOGINP')

password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
password_mgr.add_password(None, url, username, password)


handler = urllib.request.HTTPBasicAuthHandler(password_mgr)

# create "opener" (OpenerDirector instance)
opener = urllib.request.build_opener(handler)

# use the opener to fetch a URL
#opener.open(url)


# Install the opener.
# Now all calls to urllib.request.urlopen use our opener.
urllib.request.install_opener(opener)

res = urllib.request.urlopen(url)
#req = Request(url)
try:
#    response = urlopen(req)
    the_page = res.read()
    print(the_page)

except URLError as e:
    if hasattr(e, 'reason'):
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
    elif hasattr(e, 'code'):
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
else:
    # everything is fine
    print(the_page)


#request = urllib.request.urlopen(url)
#bse64string = base64.b64encode('%s:%s' % (username, password))
#headers = ["Authorization": "Basic %s" % base64string]
#result = urllib.urlopen(request)

'''
id="ta">\xcd\xe5\xf2 \xf1\xee\xee\xe1\xf9\xe5\xed\xe8\xe9          
'''
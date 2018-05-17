"""
What if we want to set a header
    1. custom header    => This may need if something else is expected by 
                            the application
    2. Fake our User-agent => To trick the server into thinking that we are the        mobile device
    3. Change the Host header  => To trick the server or load balence
    4. Brute force or temper any header  => And see how the application handles it

"""

#!/usr/bin/env

import requests


## For custom headers purpose we can make dictionary of  myheaders with what we
## we want ot change and pass parameter in requests get headers=myheaders

myheaders={'user-agent' : 'Iphone-X'}
r = requests.get('http://httpbin.org/headers', headers=myheaders)  # senging get requests for headers



print r.url

print 'Status code :'
print '\t[-]' + str(r.status_code) + '\n'

print 'Server headers'
print "*************************************************"

for x in r.headers:
    print '\t' + x + ':' + r.headers[x]

print "*************************************************"

print "Content:\n"

print r.text

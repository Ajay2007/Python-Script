import requests


## This will print 200  ok status code

url = 'http://httpbin.org/html'

req = requests.get(url)

print "Response Code : " + str(req.status_code)


# For redirected HTTP code we will redirect the url with some different 
# url say www.bing.com

url1 = 'http://httpbin.org/redirect-to'
payload = {'url':'http://www.bing.com'}

r = requests.get(url1, params=payload)

print r.text
print "Response code :"+ str(r.status_code)

# But we didn't see our redirected HTTP code. becasue redirected codes get store
# in history for retriving it we will use r.history

# r.history => is a list of all responses in the redirection chain

for x in r.history:
    print str(x.status_code) + ':' + x.url



'''Response content is the information about the server's response that is delivered back to our console when we send a request'''

'''
While interacting with the web , it's necessary to decode the response of the server. While working on an application , there are many cases in which we may have to deal with the raw, or JSON , or even binary response . For this , "requests" has thecapability to automatically decode the content from the server. Requests can smoothly decode many of the Unicode charsets. To add to that Requests makes informed gueses about the encoding of the response. This is basically happens taking the header
into consideration


Now if we access the value of r.content . it results us the response content in a raw string format. And if we access r.text, the Requests library encodes the response (r.content value) using r.encoding and returns a new encoding string. In case. if the value of r.encoding is None, Requests assumes the encoding type using r.apparent_encoding, which is provided by the chardet library

so now we can access the server's response content in the following way
'''

import requests

r = requests.get('https://google.com')

print r.content
print "ending of the r.content"
print type(r.content)
print "ending of the type of r.content"

print r.text

print "ending of the r.text"

print type(r.text)

print "ending of the type of r.texbt"

'''
So in the following code we try to get the google homapage , using requests.get()
and assining it to a variable r . The r variable turns out to be a request object here, and we can access the raw content and the encoded response content with r.text

If we wish to find what encoding Requests is using , or if we desire to change the encoding , we can use the property r.encoding to find out what encoding it is using

>>> r.encoding
'ISO-8859-1'
>>> r.encoding = 'utf-8'


In the first line of the code we are trying to access the type of encoding that is being followed by Requests. It resulted in 'ISO-8859-1'. In the next line , I am changing the encoding to 'utf-8'. So I assigned the type of encoding to r.encoding. 

If we change the encoding like we did in the second line , Requests tends to use the latest value of r.encoding that has been assigned . So from that point in time, it uses the same encoding whenever we call r.text


For  an instance , if the value of r.encoding is None, Requests tend to use the value of r.apparent-encoding. like in the example below

>>> r.encoding = None
>>> r.apparent_encoding

Generally , the value of apparent encoding is specified by the chardet library, With more enthusiasm , if we attempt to set a new encoding type to r.apparent-encoding, Requests raises an AttributeError as its value can't be altered


So Requests are efficient enough to use custom encodings. Take a case in which we have created an encoding of our own, and got it registered with the module of codecs. We can use custom codec with ease; this is because the value of r.encoding and Requests will take care of the decoding.
'''













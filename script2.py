import requests
import  urllib.request
import urllib.parse
import re

#url = 'https://www.google.com/'
url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
#url = 'https://www.w3schools.com/w3css/tryit.asp?filename=tryw3css_default_intro'

# r = requests.get(url)
# r.text
# print(r.text)
print('read website')
values = {'s':'basics', 'submit':'search' }
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read()

# print(respData) # not readable ... 

# apply regular expressions: 
# read paragraphs like: <p content dalkdjal /p>

paragraphs = re.findall(r'<p>(.*?)</p>', str(respData) )

for p in paragraphs: 
    print(p)
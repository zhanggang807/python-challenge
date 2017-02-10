#-*-encoding: utf-8-*-#

import re
from urllib import request, parse


def requestnothing(num):
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
    params = { 'nothing' : num}
    querystring = parse.urlencode(params)
    resp = request.urlopen(url + '?' + querystring)
    doc = resp.read()
    print(doc)
    return doc
    
text = requestnothing(12345)
print(text)
text = str(text)
pattern = re.compile(r'[0-9]{5}')
print(text)
match = pattern.match(text)
if match:
    print(match.group())


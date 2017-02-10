# -*- coding: utf-8 -*- #

import re
import threading
from urllib import request, parse


def requestnothing(num):
    print('param', num)
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
    params = {'nothing': num}
    querystring = parse.urlencode(params)
    resp = request.urlopen(url + '?' + querystring)
    data = resp.read()
    data = data.decode('utf-8')
    print(data)
    return data
    
if __name__ == '__main__':
    data = 12345
    # pattern = re.compile(r'[0-9]{5}')  # 为什么不通过？因为只匹配开头和结尾
    count = 0  # 一共请求了86次，最后nothing=16044，然后除以2，再赋给nothing
    # 最后出现peak.html但是我访问为什么没有出来，但是peak.html确实好使
    while True:
        # threading.sleep(2000)
        count += 1
        print('----------------', count)
        textStr = requestnothing(data)
        search = re.search(r'[0-9]{4,5}', textStr)  #搜索多处

        if search is None:
            print('finally ', int(data) / 2)
            break
        num = search.group()
        if num.isalnum():
            print(num)
            data = num
        else:
            print('none' + num)

    # print()  # 还是用search吧
    # print(textStr)
    # match = pattern.match(textStr)
    # if match:
    #     print(match.group())

    # pattern2 = re.compile(r'[0-9]{5}')
    # match2 = pattern2.match('12312.com')
    # print(match2.group())


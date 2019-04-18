#!/usr/bin/env python3
#_*_ coding: utf-8 _*_

import urllib.request
import ssl
context = ssl._create_unverified_context()
headers = {
    :authority: www.python.org
    :method: GET
    :path: /
    :scheme: https
    accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
    accept-encoding: gzip, deflate, br
    accept-language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7
    referer: https://www.google.com/
    upgrade-insecure-requests: 1
    user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36
}
response = urllib.request.urlopen('https://www.python.org/',context=context)
result = response.read().decode('utf-8')
print(response.geturl())
print(response.info())
print(response.getcode())
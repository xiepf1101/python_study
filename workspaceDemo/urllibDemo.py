#coding=utf-8
#urllib详细使用方法(header,代理,超时,认证,异常处理)

import urllib.request
response = urllib.request.urlopen('http://python.org/')
html = response.read()
print(html)

#Request 的使用
req = urllib.request.Request('http://python.org/')
response = urllib.request.urlopen(req)
page = response.read()
print(page)

#http 错误
import urllib.request

req = urllib.request.Request('http://www.111cn.net ')
try:
    e = urllib.request.urlopen(req)
except urllib.error.HTTPError as e:
    print(e.code)
print(e.read().decode("utf8"))

#异常处理
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
req = Request("http://www.111cn.net /")
try:
    response = urlopen(req)
except HTTPError as e:
    print('The server couldn’t fulfill the request.')
    print('Error code: ', e.code)
except URLError as e:
    print('We failed to reach a server.')
    print('Reason: ', e.reason)
else:
    print("good!")
print(response.read().decode("utf8"))



#Http认证

import urllib.request

# create a password manager
password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()

# Add the username and password.
# If we knew the realm, we could use it instead of None.
top_level_url = "https://www.111cn.net /"
password_mgr.add_password(None, top_level_url, 'rekfan', 'xxxxxx')

handler = urllib.request.HTTPBasicAuthHandler(password_mgr)

# create "opener" (OpenerDirector instance)
opener = urllib.request.build_opener(handler)

# use the opener to fetch a URL
a_url = "https://www.111cn.net /"
x = opener.open(a_url)
print(x.read())

# Install the opener.
# Now all calls to urllib.request.urlopen use our opener.
urllib.request.install_opener(opener)

a = urllib.request.urlopen(a_url).read().decode('utf8')
print(a)


#使用代理

import urllib.request

proxy_support = urllib.request.ProxyHandler({'sock5': 'localhost:1080'})
opener = urllib.request.build_opener(proxy_support)
urllib.request.install_opener(opener)
a = urllib.request.urlopen("http://www.111cn.net").read().decode("utf8")
print(a)


#超时

import socket
import urllib.request

# timeout in seconds
timeout = 2
socket.setdefaulttimeout(timeout)

# this call to urllib.request.urlopen now uses the default timeout
# we have set in the socket module
req = urllib.request.Request('http://www.111cn.net /')
a = urllib.request.urlopen(req).read()
print(a)



#发送数据
import urllib.parse
import urllib.request

url = 'http://localhost/login.php'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {
'act' : 'login',
'login[email]' : '1230@qq.com',
'login[password]' : '123456'
}

data = urllib.parse.urlencode(values)
req = urllib.request.Request(url, data)
req.add_header('Referer', 'http://python.org/')
response = urllib.request.urlopen(req)
the_page = response.read()

print(the_page.decode("utf8"))

#发送数据和header
import urllib.parse
import urllib.request

url = 'http://localhost/login.php'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {
'act' : 'login',
'login[email]' : 'yzhang@i9i8.com',
'login[password]' : '123456'
}
headers = { 'User-Agent' : user_agent }

data = urllib.parse.urlencode(values)
req = urllib.request.Request(url, data, headers)
response = urllib.request.urlopen(req)
the_page = response.read()

print(the_page.decode("utf8"))
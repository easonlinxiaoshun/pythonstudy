import  requests

url='https://sam.huat.edu.cn:8443/selfservice'

#各种网站很多代理地址
proxies={
    'http':'http://14.215.212.37:9168',
    # 'https':'https://14.215.212.37:9168'
}

#timeout设置为3秒.  proxies代理参数.  verify=False设置忽略CA证书认证直接访问，但会有警告提示
response=requests.get(url,timeout=5,proxies=proxies,verify=False)

print(response.cookies)

dict_cookies=requests.utils.dict_from_cookiejar(response.cookies)
print(dict_cookies)

jar_cookies=requests.utils.cookiejar_from_dict(dict_cookies)
print(jar_cookies)
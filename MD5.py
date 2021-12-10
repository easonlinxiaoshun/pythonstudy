import  requests
import re
import js2py
# url='https://www.cmd5.com/md5.js'
# context=js2py.EvalJs()
# with open('md5.js', 'r', encoding='utf-8') as f:
#     context.execute(f.read())
# # headers={
# # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
# # }
# #
# # response=requests.get(url,headers=headers)
# #
#
#
# context.execute("var t= md5('123456', 0);")
# print(context.t)

url='http://tool.sufeinet.com/Encrypt/MD5.aspx?'

headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
}
data = {
    'action': 'Encode',
    'md5str':'4297f44b13955235245b2497399d7a93'
}

temp='td_cookie=3288937730; security_session_verify=c57b3647158f1f9ef17478b257862155; ASP.NET_SessionId=dnwxf5ojtrabwbkk2e1ai304; Hm_lvt_66f619b1063cb3d8c97e3984b837fa07=1639125119; Hm_lpvt_66f619b1063cb3d8c97e3984b837fa07=1639125119'
cookie_list=temp.split(';')
cookies={}
#for cookie in cookie_list:
#    cookies[cookie.split('=')[0]]=cookie.split('=')[-1]

cookies={cookie.split('=')[0]:cookie.split('=')[-1]for cookie in cookie_list}

response=requests.get(url,headers=headers,params=data)

res_1=response.content.decode()

#start 手动设定编码格式
#response.encoding='utf8'
#打印源码str类型数据
#print(response.text)
#end

#content是存储bytes类型的响应源码，可以进行decode操作,默认utf8
#print(response.content.decode())

print(response.cookies)

timestamp_secret = re.findall('id="rightcp_txtmd5" cols="78" rows="5" class="form-control" style="width:725px">(.*?)</textarea>', res_1)[0]
print(timestamp_secret)

with open('md5.html','wb')as f:
    f.write(response.content)
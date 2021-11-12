import  requests
import re

def login():
    # session
    session=requests.session()
    # headers
    session.headers={
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
    }
    # url1-获取token
    url1='https://github.com/login'
    # 发送请求获取响应
    res_1=session.get(url1).content.decode()
    # 正则提取
    token=re.findall('name="authenticity_token" value="(.*?)" />',res_1)[0]
    timestamp=re.findall('name="timestamp" value="(.*?)" autocomplete="off" class="form-control" />',res_1)[0]
    timestamp_secret = re.findall('name="timestamp_secret" value="(.*?)" autocomplete="off" class="form-control" />', res_1)[0]
    print(token)

    # url2-登录
    url2='https://github.com/session'
    # 构建表单数据
    data={
        "commit": "Sign in",
        "authenticity_token": token,
        "login": "easonlinxiaoshun",
        "password": "easonp@ssw0rd",
        "webauthn-support":"supported",
        "webauthn-iuvpaa-support":"unsupported",
        "return_to": "https://github.com/login",
        "timestamp": timestamp,
        "timestamp_secret": timestamp_secret,
    }
    # 发送请求登录
    session.post(url2,data=data)
    # url3-验证
    url3='https://github.com/easonlinxiaoshun'
    response=session.get(url3)
    with open('github.html','wb')as f:
        f.write(response.content)

if __name__=='__main__':
    login()
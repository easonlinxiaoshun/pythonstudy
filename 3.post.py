import  requests
import  js2py
import json
class baidutranslate(object):
    def __init__(self,word):
        self.url='https://fanyi.baidu.com/v2transapi'
        self.headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
            'Referer': 'https://fanyi.baidu.com/?aldtype=16047',
        }
        temp = 'BIDUPSID=9A24629512C0F13BD39FFAEC9DA075A7; PSTM=1618223890; BAIDUID=9A24629512C0F13B0F659E7D5AF0845F:FG=1; __yjs_duid=1_d808ee7c37696a8462e0de64e2eecb4c1618557830693; REALTIME_TRANS_SWITCH=1; HISTORY_SWITCH=1; FANYI_WORD_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDUSS=FRUGlYQkpvQVEwamRsdmtRNXlwcFVRY3dxRmxmVDZaQzZWazhkaWgyQkpXcjlnRVFBQUFBJCQAAAAAAAAAAAEAAADWpmxrtPe2-rv68fbM~QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEnNl2BJzZdgbW; BDUSS_BFESS=FRUGlYQkpvQVEwamRsdmtRNXlwcFVRY3dxRmxmVDZaQzZWazhkaWgyQkpXcjlnRVFBQUFBJCQAAAAAAAAAAAEAAADWpmxrtPe2-rv68fbM~QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEnNl2BJzZdgbW; MCITY=-%3A; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDSFRCVID=XWuOJeCT5G3_WP5HZhBQUC7BNeKKN9OTTPjcTR5qJ04BtyCVNKsaEG0PtOgMNBDbJ2MRogKK3gOTH4DF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tJ4toCPMJI_3fP36q45HMt00qxby26nvQ5T9aJ5nQI5nhU7505o1W4kY0JomtMjw5m3i2DTvQUbmjRO206oay6O3LlO83h5wW57KKl0MLPbcep68LxODy6DI0xnMBMPe52OnaIbg3fAKftnOM46JehL3346-35543bRTLnLy5KJYMDcnK4-Xj5jbeabP; BDSFRCVID_BFESS=XWuOJeCT5G3_WP5HZhBQUC7BNeKKN9OTTPjcTR5qJ04BtyCVNKsaEG0PtOgMNBDbJ2MRogKK3gOTH4DF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tJ4toCPMJI_3fP36q45HMt00qxby26nvQ5T9aJ5nQI5nhU7505o1W4kY0JomtMjw5m3i2DTvQUbmjRO206oay6O3LlO83h5wW57KKl0MLPbcep68LxODy6DI0xnMBMPe52OnaIbg3fAKftnOM46JehL3346-35543bRTLnLy5KJYMDcnK4-Xj5jbeabP; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1636102660,1636597892,1636612251; ab_sr=1.0.1_Mjg4MTViNzU5MzM1YTIwYTJkMGJjMjBmMWU1ZDRkNmQ3NDc5NmQ1ZDVkYjU0NzU1MjE4Yjg4YjliZDBkOGQ1NDFhOWJmNDYzNzhjZmRhM2QwOTEzYTY2M2UwOTg1NmJlYmM1MzY5ODg5NTVhYTAyYTk0MWIyMDViMDc2YzYwOTNlOGRiYjM3MGViZjM5OTdjNGJmYjc5ZjJlZmQ5MzNiZWFlYTQ0ZTcwZmJlZTIwYTIxNjgwYzVmZGZlOWQ3NjYz; delPer=0; PSINO=6; H_PS_PSSID=34946_31660_35054_34903_35063_34517_34813_26350_34973_34867_34993; BA_HECTOR=2ha1018h2k2g8k809e1gopmf90r; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1636621228'
        cookie_list = temp.split(';')
        self.cookies = {}
        self.cookies = {cookie.split('=')[0]: cookie.split('=')[-1] for cookie in cookie_list}
        self.word=word
        self.sign =self.get_sign(word)
        self.data={
        "from": "zh",
        "to": "en",
        "query": word,
        "simple_means_flag": "3",
        "sign": self.sign,
        "token": "960ccdf5c35e0f353aacf52b22a33349",
        "domain": "common"
        }


    def get_data(self):
        response=requests.post(self.url,data=self.data,headers=self.headers,cookies=self.cookies)
        print(self.data)
        return response.content

    def get_sign(self,word):
        # 创建上下文对象
        context = js2py.EvalJs()
        # 执行js获得结果
        with open('百度翻译的.js', 'r', encoding='utf-8') as f:
            context.execute(f.read())
        sign = context.e(word)
        print('sign', sign)
        return sign

    def run(self):
        #编写爬虫逻辑

        #url
        #headers
        #datd字典
        #发送请求获取响应
        response=self.get_data()
        print(response.decode('unicode_escape'))
        #数据解析


if __name__=='__main__':
    Baidutranslate=baidutranslate('字典')
    Baidutranslate.run()

#coding:utf-8
import requests
from lxml import etree
class Tieba(object):
    def __init__(self,name):
        self.url="https://tieba.baidu.com/f?ie=utf-8&kw={}".format(name)
        self.headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
            # "User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)"#方法二 低端浏览器获取的html不被注释
        }


    def get_data(self,url):
        response=requests.get(url,headers=self.headers)
        return response.content

    def parse_data(self,data):
        #创建element对象
        #方法一 高端浏览器将注释符去掉就可以获取规定数据
        data=data.decode().replace("<!--","").replace("-->","")
        html=etree.HTML(data)
        el_list=html.xpath('//*[@id="thread_list"]/li/div/div[2]/div[1]/div[1]/a')
        # print(len(el_list))

        data_list=[]
        for el in el_list:
            temp={}
            temp['title']=el.xpath("./text()")[0]
            temp['link']='https://tieba.baidu.com/'+el.xpath("./@href")[0]
            data_list.append(temp)

        #循环下一页
        try:
            # next_url='https:'+html.xpath('//a[@class="next pagination-item"]/@href')[0]
            next_url = 'https:' + html.xpath('//a[contains(text(),"下一页")]/@href')[0]
        except:
            next_url=None

        return data_list,next_url

    def save_data(self,data_list):
        for data in data_list:
            print(data)


    def run(self):
        next_url=self.url
        while True:
            data=self.get_data(next_url)
            data_list,next_url=self.parse_data(data)

            self.save_data(data_list)

            if next_url ==None:
                break


if __name__ == '__main__':
    tieba=Tieba("哈密波")
    tieba.run()
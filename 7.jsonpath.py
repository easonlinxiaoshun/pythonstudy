# from jsonpath import jsonpath
# import json
# data={'key1':{'key2':{'key3':{'key4':{'key5':{'key6':'python'}}}}}}
#
# print(data['key1']['key2']['key3']['key4']['key5']['key6'])
#
# #print(jsonpath(data,'$.key1.key2.key3.key4.key5.key6')[0])
# print(jsonpath(data,'$..key6')[0])
#
# data2='''{"new_product_code":"310211131001","new_accountsort2":"A; B","accountsort":[{"Value":1,"Text":"A"},{"Value":2,"Text":"B"}],"accountsortstr":["A","B"],"accountsortint":[1,2],"new_price":"222.00"}'''
#
# datachan=json.loads(data2)
# print(jsonpath(datachan,"$..Value"))

import requests
from lxml import etree

text='''
<div class="u-err f-hide">
    <i class="u-icn u-icn-25"></i>
    <span></span>
</div>
<div class="pwd-validation f-hide">
    <div class="j-err u-err j-pwd-valid">
        <i class="u-icn"></i>
        <span>密码不能包含空格</span>
    </div>
    <div class="j-err u-err j-pwd-valid">
        <i class="u-icn"></i>
        <span>包含字母、数字、符号中至少两种</span>
    </div>
    <div class="j-err u-err j-pwd-valid">
        <i class="u-icn"></i>
        <span>密码长度为8-20位</span>
    </div>
</div>'''

#创建element对象
html=etree.HTML(text)
el_list=html.xpath('/div[@class=""]')
# print(html)
# print(dir(html))
print(html.xpath('//div[@class="j-err u-err j-pwd-valid"]/span/text()'))
print(html.xpath('//div[@class="j-err u-err j-pwd-valid"]/span/text()')[0])
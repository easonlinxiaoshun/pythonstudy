#encoding=utf-8
import xlrd
from xlutils.copy import copy
from xlwt import *
import  requests
import re
url='http://tool.sufeinet.com/Encrypt/MD5.aspx?'

headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
}

#------------------读数据---------------------------------
fileName="c:\\Users\\Administrator\\Desktop\\text2.xls"
bk=xlrd.open_workbook(fileName)
shxrange=range(bk.nsheets)
try:
    sh=bk.sheet_by_name("Sheet1")
    new_workbook = copy(bk)  # 将xlrd对象拷贝转化为xlwt对象
    new_worksheet = new_workbook.get_sheet(0)  # 获取转化后工作簿中的第一个表格

except:
    print("代码出错")
nrows=sh.nrows #获取行数
for i in range(1,nrows):
    row_data=sh.cell_value(i,0)
    data = {
        'action': 'Encode',
        'md5str': row_data
    }
    #获取第i行第3列数据
    #sh.cell_value(i,3)
    #---------写出文件到excel--------
    print("-----正在写入 "+str(i)+" 行")
    response = requests.get(url, headers=headers, params=data)

    res_1 = response.content.decode()
    timestamp_secret = re.findall('id="rightcp_txtmd5" cols="78" rows="5" class="form-control" style="width:725px">(.*?)</textarea>',res_1)[0]
    new_worksheet.write(i,1, timestamp_secret)
new_workbook.save("c:\\Users\\Administrator\\Desktop\\text2.xls")
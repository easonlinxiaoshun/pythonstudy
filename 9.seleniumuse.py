import time
from selenium import webdriver

#已经添加浏览器驱动的环境变量
driver=webdriver.Chrome()

#控制浏览器访问url地址
driver.get("https://www.baidu.com")

# 百度搜索栏中输入python
driver.find_element_by_id('kw').send_keys('python')

# 点击搜索
driver.find_element_by_id('su').click()

time.sleep(6)

#退出浏览器
driver.quit()
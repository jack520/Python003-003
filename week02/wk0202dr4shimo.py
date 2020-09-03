'''
Selenium 模拟登录石墨文档 https://shimo.im

name="mobileOrEmail"

name="password"

<button class="sm-button submit sc-1n784rm-0 bcuuIb" type="black">立即登录</button>
xpath = r'//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/button'

'''

# 导入库
from selenium import webdriver
import time

#打开浏览器，打开 login 页面
driver=webdriver.Chrome()
driver.get("https://shimo.im/login?from=home")
time.sleep(5)

# 通过name查找，然后输入用户名和密码

username='15612335123'
password='123456789ab'

driver.find_element_by_name("mobileOrEmail").send_keys(username)
time.sleep(5)
print('sent phone number')

driver.find_element_by_name("password").send_keys(password)
time.sleep(5)
print('sent password')

# 立即登录 button

xpath = r'//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/button'
driver.find_element_by_xpath(xpath).click()
print('clicked')


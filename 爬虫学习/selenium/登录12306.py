from selenium.webdriver import Chrome
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

option=Options()
option.add_argument('--disable-blink-features=AutomationControlled')

web=Chrome(options=option)

web.get("https://kyfw.12306.cn/otn/resources/login.html")

web.find_element_by_xpath('//*[@id="J-userName"]').send_keys('13430862288')
web.find_element_by_xpath('//*[@id="J-password"]').send_keys('zhengjiahao418')
web.find_element_by_xpath('//*[@id="J-login"]').click()
time.sleep(1)

# 滑动验证
btn=web.find_element_by_xpath('//*[@id="nc_1_n1z"]')
ActionChains(web).drag_and_drop_by_offset(btn,300,0).perform()
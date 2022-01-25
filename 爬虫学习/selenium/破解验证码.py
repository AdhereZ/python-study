from selenium.webdriver import Chrome
import time
from selenium.webdriver.common.keys import Keys
from chaojiying import Chaojiying_Client

web=Chrome()
web.get('http://www.chaojiying.com/user/login/')

#截屏
img=web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/div/img').screenshot_as_png

chaojiying = Chaojiying_Client('adhere418', 'zhengjiahao418', '928097')	
dic=chaojiying.PostPic(img, 1902)
str=dic['pic_str']

username=web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input').send_keys('adhere418')
password=web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input').send_keys('zhengjiahao418')
vc=web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input').send_keys(str)
time.sleep(3)

web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input').click()
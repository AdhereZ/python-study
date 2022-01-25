from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys

import time

web=Chrome()

web.get("https://lagou.com")

el=web.find_element_by_xpath('//*[@id="changeCityBox"]/p[1]/a')

el.click()

time.sleep(1) #让浏览器缓一会

web.find_element_by_xpath('//*[@id="search_input"]').send_keys('python',Keys.ENTER)

time.sleep(1)

divs=web.find_elements_by_xpath('//*[@id="jobList"]/div[1]/div')
for d in divs:
  wname=d.find_element_by_xpath('./div[1]/div[1]/div[1]/a').text
  money=d.find_element_by_xpath('./div[1]/div[1]/div[2]/span').text
  cname=d.find_element_by_xpath('./div[1]/div[2]/div[1]/a').text
  print(wname,money,cname)

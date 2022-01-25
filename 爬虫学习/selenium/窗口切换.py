from selenium.webdriver import Chrome
import time
from selenium.webdriver.common.keys import Keys

web=Chrome()

web.get("https://lagou.com")


el=web.find_element_by_xpath('//*[@id="changeCityBox"]/p[1]/a')

el.click()

time.sleep(1) #让浏览器缓一会

web.find_element_by_xpath('//*[@id="search_input"]').send_keys('python',Keys.ENTER)

time.sleep(1)

web.find_element_by_xpath('//*[@id="jobList"]/div[1]/div[1]/div[1]/div[1]/div[1]/a').click()
web.switch_to.window(web.window_handles[-1])


detail=web.find_element_by_xpath('//*[@id="job_detail"]/dd[2]/div').text

print(detail)

time.sleep(1)

web.close()
web.switch_to.window(web.window_handles[0])
print(web.find_element_by_xpath('//*[@id="jobList"]/div[1]/div[1]/div[1]/div[1]/div[1]/a').text)


iframe=web.find_element_by_xpath('//*[@id="player_iframe]')
web.switch_to_frame(iframe)
web.switch_to_default_content() #切回原来窗口
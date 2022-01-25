import imp
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.chrome.options import Options

opt=Options()
opt.add_argument('--headless')
opt.add_argument('--disable-gpu')

web=Chrome(options=opt)

web.get("https://www.endata.com.cn/BoxOffice/BO/Year/index.html")
time.sleep(2)

# select = web.find_element_by_xpath('//*[@id="OptionDate"]')

# # 对元素进行包装
# sel=Select(select)

# for i in range(len(sel.options)):
#   sel.select_by_index(i)
#   time.sleep(2)
#   table=web.find_element_by_xpath('//*[@id="TableList"]/table')
#   print(table.text)
#   print('=================================')

# web.close()


# 获取页面代码 (经过网络请求后并且被js处理过的代码)
print(web.page_source)


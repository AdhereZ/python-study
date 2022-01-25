from selenium.webdriver import Chrome
import time

web=Chrome()

if __name__ == '__main__':
  

  web.get("https://www.baidu.com/")
  print(web.title)

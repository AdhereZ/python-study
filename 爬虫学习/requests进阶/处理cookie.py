import re
import requests

session=requests.session()

data = {
  "loginName": "18614075987",
  "password": "q6035945"
}
res=session.post("https://passport.17k.com/ck/user/login",data=data)
# print(res.cookies)

res1=session.get("https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919")
print(res1.json())

# 手动加上cookies也行，比较麻烦
# res2=requests.get("https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919",headers={
#   "Cookie": "GUID=e9b18e30-268a-4094-9bd3-1fdafe381e10; BAIDU_SSP_lcr=https://www.baidu.com/link?url=hU87xeFj3eJL3XPfC7FY61BIp-d9X-wylm7fGgJwNuO&wd=&eqid=ae6479a60004a5750000000661e7ca4f; sajssdk_2015_cross_new_user=1; Hm_lvt_9793f42b498361373512340937deb2a0=1642580565; c_channel=0; c_csc=web; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F16%252F16%252F64%252F75836416.jpg-88x88%253Fv%253D1610625030000%26id%3D75836416%26nickname%3D%25E9%25BA%25BB%25E8%25BE%25A3%25E5%2587%25A0%25E4%25B8%259D%26e%3D1658133834%26s%3Dc9821c4ad3517e2c; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2275836416%22%2C%22%24device_id%22%3A%2217e716e5b9ca4c-0dfe1d5c77319f-f791b31-2073600-17e716e5b9d5a0%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%2C%22first_id%22%3A%22e9b18e30-268a-4094-9bd3-1fdafe381e10%22%7D; Hm_lpvt_9793f42b498361373512340937deb2a0=1642581872"
# })

# print(res2.json())


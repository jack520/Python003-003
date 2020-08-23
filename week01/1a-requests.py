import requests

user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3766.400 QQBrowser/10.6.4163.400"
header = {'user-agent':user_agent}

myurl = "https://movie.douban.com/top250"

response = requests.get(myurl,headers=header)

print(response.text)
print(f'返回码是：{response.status_code}')
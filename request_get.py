import requests
import re


def login():
    # session
    session = requests.session()
    # headers
    session.headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
    }
    # url1获取token
    url = 'https://github.com/login'
    # 发送请求获得响应
    res_1 = session.get(url).content.decode()

    # 正则提取
    token = re.findall('name="authenticity_token" value="(.*?)" />', res_1)[0]
    print(token)
    # url2登录
    url2 = 'https://github.com/session'
    # 构建表单数据
    data = {
        'commit': 'Sign in',
        'utf8': '√',
        'authenticity_token': token,
        'login': '用户名',
        'password': '密码',
        'webauthn-support': 'supported'
    }

    # 发送请求登录
    session.post(url2, data=data)
    # url3验证
    url3 = 'https://github.com/用户名'
    response = session.get(url3)
    with open('github.html', 'wb')as f:
        f.write(response.content)


if __name__ == '__main__':
    login()

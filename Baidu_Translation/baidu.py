# !/user/bin/env python
# -*- coding:utf-8 -*- 
# time: 2018/7/21--10:21
__author__ = 'Henry'

'''
百度翻译
'''

import requests
import execjs

while True:
    word = input('请输入您要翻译的单词:')
    with open('baidu.js', encoding='utf-8') as f:
        jsdata = f.read()

    p = execjs.compile(jsdata).call('e', word)  # 加密后的sign值

    form = {
        'from': 'zh',
        'to': 'en',
        'query': word,
        'transtype': 'realtime',
        'simple_means_flag': '3',
        'sign': p,
        'token': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',  # 固定的(带入你自己的token)
    }
    if word >= u'\u4e00' and word <= u'\u9fa6':  # 如果含有中文时
        pass
    else:  # 英->中
        form['from'], form['to'] = form['to'], form['from']
    url = 'https://fanyi.baidu.com/v2transapi'
    headers = {
        'Cookie': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',  # 固定的(带入你自己的cookie)
        'Host': 'fanyi.baidu.com',
        'Origin': 'http://fanyi.baidu.com',
        'Referer': 'http://fanyi.baidu.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    }
    html = requests.post(url=url, data=form, headers=headers).json()
    content = html['trans_result']['data']
    for i in content:
        result = i['dst']
        print('译文:' + result)

# 运行前请先修改form中的token,还有headers中的cookie,抓包一次即可获得!!!

# !/user/bin/env python
# -*- coding:utf-8 -*- 
# time: 2018/9/29--14:52
__author__ = 'Henry'

'''
必应翻译
'''

import requests

while True:
    word = input('请输入您要查询的单词:')
    data = {
        'text': word,
        'from': 'en',
        'to': 'zh-CHS'
    }
    if word >= u'\u4e00' and word <= u'\u9fa6':  # 如果含有中文时
        data['from'], data['to'] = data['to'], data['from']
    url = 'https://cn.bing.com/ttranslate?&category=&IG=68513C1D58404825BC0EB549E11C4F92&IID=translator.5036.3'
    headers = {
        'referer': 'https://cn.bing.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    }
    res = requests.post(url, data=data, headers=headers).json()
    result = res.get('translationResponse', 'No Result~')
    print('译文:' + result)

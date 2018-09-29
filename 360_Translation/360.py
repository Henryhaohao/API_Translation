# !/user/bin/env python
# -*- coding:utf-8 -*- 
# time: 2018/9/29--16:02
__author__ = 'Henry'

'''
360翻译
'''

import requests

while True:
    key = input('请输入您要翻译的内容:')
    if key >= u'\u4e00' and key <= u'\u9fa6':  # 如果含有中文时
        eng = 0
    else:  # 否则为英文
        eng = 1
    url = 'https://fanyi.so.com/index/search'
    form = {
        'query': key,
        'eng': str(eng)
    }
    html = requests.post(url, data=form).json()
    print('译文:' + html['data']['fanyi'])

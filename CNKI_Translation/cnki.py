# !/user/bin/env python
# -*- coding:utf-8 -*- 
# time: 2018/9/29--14:54
__author__ = 'Henry'

'''
CNKI翻译
'''

import requests
import re

while True:
    key = input('请输入您要翻译的单词:')

    url = 'http://dict.cnki.net/dict_result.aspx?searchword=%s' % key
    html = requests.get(url).text
    # print(html)
    reg = r'<meta content=".*?  的翻译结果：(.*?)双语例句.*?英文例句.*?相关文摘"'
    res = re.findall(reg, html, re.S)[0][:-2]
    print('译文:' + res)

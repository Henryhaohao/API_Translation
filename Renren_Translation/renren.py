# !/user/bin/env python
# -*- coding:utf-8 -*- 
# time: 2018/9/29--16:05
__author__ = 'Henry'

'''
人人翻译
特点:有美剧场景例句; 缺点:不能翻译句子,只能单词
'''

import requests
import re

while True:
    key = input('请输入您要翻译的单词:')
    url = 'http://www.91dict.com/words?w=%s' % key
    html = requests.get(url).text
    # print(html)
    content = re.findall(r'class="listBox">(.*?)<div', html, re.S)[0].replace('\n', '').replace('<br>', '')
    # print(content)
    if key >= u'\u4e00' and key <= u'\u9fa6':  # 如果含有中文时
        reg = r'<a href="/words.*?">(.*?)</a>'
        result = re.findall(reg, content, re.S)
        print('译文:')
        for i in result:
            if i != 'int' and i != 'vi' and i != 'n' and i != 'adj' and i != 'pron' and i != 'misc':
                print(i, end='')
                print(';', end='')
        print('\n')
    else:  # 否则为英文时
        print('译文:' + content)

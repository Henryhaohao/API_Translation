# !/user/bin/env python
# -*- coding:utf-8 -*- 
# time: 2018/8/17--12:45
__author__ = 'Henry'

'''
谷歌翻译
'''

import requests, execjs

while True:
    word = input('请输入您要翻译的单词:')
    with open('google.js', encoding='utf-8') as f:
        jsdata = f.read()
    tk = execjs.compile(jsdata).call('tk', word)
    # print(tk)

    if word >= u'\u4e00' and word <= u'\u9fa6':  # 如果含有中文时
        url = 'https://translate.google.cn/translate_a/single?client=t&sl=zh-CN&tl=en&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&source=bh&ssel=0&tsel=0&kc=1&tk={}&q={}'.format(
            tk, word)
    else:
        url = 'https://translate.google.cn/translate_a/single?client=t&sl=en&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&source=bh&ssel=0&tsel=0&kc=1&tk={}&q={}'.format(
            tk, word)
    headers = {
        'referer': 'https://translate.google.cn/',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    }
    res = requests.get(url, headers=headers).json()
    result = res[0][0][0]
    print('译文:' + result)

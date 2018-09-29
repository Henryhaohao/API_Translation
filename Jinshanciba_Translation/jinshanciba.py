# !/user/bin/env python
# -*- coding:utf-8 -*- 
# time: 2018/9/29--14:50
__author__ = 'Henry'

'''
金山词霸
'''
import requests
import re

while True:
    key = input('请输入你要翻译的内容:')
    url = 'http://fy.iciba.com/ajax.php?a=fy'
    form = {'f': 'auto', 't': 'auto', 'w': key}
    html = requests.post(url, data=form).json()

    try:
        req_1 = html['content']['out']
        req_2 = re.sub(r'<br/>', '', req_1)  # 如果结果含有</br>,就删掉它(当原文不是中文也不是英文时:要去掉后面带的</br>)
        print('译文:' + req_2)
    except:
        req = html['content']['word_mean']
        print('译文:')
        for i in range(len(req)):
            print(req[i])

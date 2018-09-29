# !/user/bin/env python
# -*- coding:utf-8 -*- 
# time: 2018/8/2--21:34
__author__ = 'Henry'

'''
有道翻译
'''

import requests, time, random, hashlib

while True:
    key = input('请输入您要翻译的内容:')
    # salt盐值:  (毫秒时间戳加上一个0~10的随机数)
    a = int(time.time() * 1000)
    b = random.randint(0, 10)
    salt = str(a + b)
    # sign签名值 (翻译内容+盐后的md5值)
    sign_str = "fanyideskweb" + key + salt + "ebSeFb%=XZ%T[KZ)c(sy!"
    sign = hashlib.md5(sign_str.encode('utf-8')).hexdigest()
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    data = {
        'i': key,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': salt,
        'sign': sign,
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTIME',
        'typoResult': 'false',
    }
    headers = {
        'Content-Length': str(len(data)),
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Referer': 'http://fanyi.youdao.com/',
        'Cookie': 'DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; OUTFOX_SEARCH_USER_ID=1347235677@36.63.14.212; JSESSIONID=abcrATVr6lm8p688NA1tw; OUTFOX_SEARCH_USER_ID_NCOO=99125029.28635417; _ntes_nnid=92d4d07d0e0d5f01a6694eeb3e866807,1533125764896; YOUDAO_FANYI_SELECTOR=OFF; UM_distinctid=164facace7e2bd-0597568afb261b-6b1b1279-1fa400-164facace7f877; ___rl__test__cookies=1533218374270'
        # 注意:cookie必须加上,不然就是出错 {‘errorcode’:50}
    }
    res = requests.post(url=url, headers=headers, data=data).json()
    result = res['translateResult'][0][0]['tgt']
    print('译文:' + result)

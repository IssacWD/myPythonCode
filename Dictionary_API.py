#!/usr/bin/python3
# coding=utf-8
#********************************************************
#   > OS     : Ubuntu 14.04
#	> Author : JasonGUTU
#	> Mail   : intergujinjin@foxmail.com
#	> Time   : 2016/2/4
#********************************************************

'''
有道翻译API
API key：2110071943
keyfrom：magkathea
创建时间：2016-02-04
网站名称：magkathea
网站地址：http://magkathea.com
 http://fanyi.youdao.com/openapi.do?keyfrom=magkathea&key=2110071943&type=data&doctype=<doctype>&version=1.1&q=要翻译的文本
'''
# import os
# import sys
import urllib.parse, urllib.request
import json


API_KEY = '2110071943'
KEYFROM = 'magkathea'

def get_translation_YouDao(txt):
    url = 'http://fanyi.youdao.com/openapi.do'
    data = {
        'keyfrom':KEYFROM,
        'key':API_KEY,
        'type':'data',
        'doctype':'json',
        'version':1.1,
        'q':txt
    }
    url = url + '?' + urllib.parse.urlencode(data)
    response_bytes = urllib.request.urlopen(urllib.request.Request(url)).read()
    response = str(response_bytes, encoding = 'utf-8')
    try:
        result = json.loads(response)
        return result
    except ValueError:
        pass

# YouDao
# {
#     "errorCode":0
#     "query":"good",
#     "translation":["好"], // 有道翻译
#     "basic":{ // 有道词典-基本词典
#         "phonetic":"gʊd"
#         "uk-phonetic":"gʊd" //英式发音
#         "us-phonetic":"ɡʊd" //美式发音
#         "explains":[
#             "好处",
#             "好的",
#             "好"
#         ]
#     },
#     "web":[ // 有道词典-网络释义
#         {
#             "key":"good",
#             "value":["良好","善","美好"]
#         },
#         {...}
#     ]
# }

def S_json_YouDao(json_data):
    query = json_data.get('query', '')
    translation = json_data.get('translation', '')
    basic = json_data.get('basic', '')
    sequence = json_data.get('web',[])
    phonetic = ''
    explains_txt = ''
    log_word_explains = ''
    if basic:
        phonetic = basic.get('phonetic','')
        explains = basic.get('explains',[])
        for obj in explains:
            explains_txt += obj+'\n'
            log_word_explains += obj+','
    seq_txt = ''
    if sequence:
        for obj in sequence:
            seq_txt += obj['key']+'\n'
            values = ''
            for i in obj['value']:
                values += i+','
            seq_txt += values+'\n'

    print('*' * 40)
    print('查询对象:  %s [%s]\n' % (query, phonetic))
    print(explains_txt)
    print('-' * 20 + '\n' + seq_txt)
    print('*' * 40)

def main():
    while True:
        txt = input('请输入要查询的文本：\n')
        if txt:
            S_json_YouDao(get_translation_YouDao(txt))

if __name__ == '__main__':
    main()

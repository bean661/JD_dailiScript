#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: Bean
# datetime:2023/1/16 18:36

#实现功能 添加当前公网ip到携取白名单
#携取代理 注册链接：https://www.xiequ.cn/index.html?92fd9f33

import requests

#获取白名单url 可不填
bmd_url=""

#删除所有连接
del_all_url=""

#添加白名单连接 格式(删除掉复制的"白名单IP")：http://op.xiequ.cn/IpWhiteList.aspx?uid=xxxxx&ukey=xxxxxx&act=del&ip=
add_url=""

def get_bmd():
    #获取白名单url
    url = bmd_url
    session = requests.session()
    headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                }

    response = session.get(url=url, headers=headers, verify=False)
    msg = (response.text).split(',')
    return msg

def del_all():
    # 获取白名单url
    url = ""
    session = requests.session()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    }

    response = session.get(url=del_all_url, headers=headers, verify=False)
    msg = response.text
    if msg=="success":
        print("删除成功")
    return msg
def get_ip():
    res = requests.get('http://myip.ipip.net', timeout=5).text
    ip=res[6:21]
    print(res[6:21])
    return ip
# print(del_all())
def add_bmd(new_ip):
    #获取白名单url
    url = add_url+new_ip
    session = requests.session()
    headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                }

    response = session.get(url=url, headers=headers, verify=False)
    msg = response.text
    if msg=="success":
        print("添加ip："+new_ip+"成功")
    return msg

if __name__ == '__main__':
    del_all()
    new_ip = get_ip()
    add_bmd(new_ip)

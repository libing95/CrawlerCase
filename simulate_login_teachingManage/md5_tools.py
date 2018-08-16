# -*- coding: utf-8 -*-
# @Time    : 2018/8/4 13:39
# @Author  : GarryXie

import md5

# function chkpwd(obj) {
#     if (obj.value != '') {
#         var s = md5(document.all.txt_asmcdefsddsd.value
#      + md5(obj.value).substring(0, 30).toUpperCase() + '10465').substring(0, 30).toUpperCase();
#         document.all.dsdsdsdsdxcxdfgfg.value = s;
#     } else {
#         document.all.dsdsdsdsdxcxdfgfg.value = obj.value;
#     }
# }
#
# function chkyzm(obj) {
#     if (obj.value != '') {
#         var s = md5(md5(obj.value.toUpperCase()).substring(0, 30).toUpperCase() + '10465').substring(0, 30).toUpperCase();
#         document.all.fgfggfdgtyuuyyuuckjg.value = s;
#     } else {
#         document.all.fgfggfdgtyuuyyuuckjg.value = obj.value.toUpperCase();
#     }
# }

def md5_encrypt(src):
    """
    md5 加密
    :param src: 需要加密的字段
    :return:
    """
    m1 = md5.new()
    m1.update(src.encode(encoding='utf-8'))
    return m1.hexdigest()

def md5_pwd(username, pwd):
    '''
    密码md5加密
    :param pwd:
    :return:
    '''
    return md5_encrypt((username + md5_encrypt(pwd)[0:30].upper() + '10465'))[0:30].upper()

def md5_yzm(yzm):
    '''
    验证码MD5加密
    :param yzm:
    :return:
    '''
    return md5_encrypt((md5_encrypt(yzm.upper())[0:30].upper() + '10465'))[0:30].upper()


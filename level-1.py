# -*- coding: utf-8 -*-


def move_char(ch):
    ch_new = ''
    if 'z' >= ch >= 'a':
        if ch == 'y':
            ch_new = 'a'
        elif ch == 'z':
            ch_new = 'b'
        else:
            ch_new = chr(ord(ch) + 2)  # 我的方法
    else:
        ch_new = ch

    return ch_new



str = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp.
 bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle
 qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""

# i hope you did not translate it by hand. thats what
# computers are for. doing it in by hand is inefficient and
# that's why this text is so long. using string.maketrans()
# is recommended. now apply on the url

str2 = 'map'
str_result = ''
for ch in str2:
    str_result += move_char(ch)
print(str2)
print(str_result)

# level 1
#import string  # 新版本不需要
table = str.maketrans('abcdefghijklmnopqrstuvwxyz', 'cdefghijklmnopqrstuvwxyzab')
print(str)
print('--------------------------')
# 标准方法
print(str.translate(table))
print('--------------------------')
print(str2.translate(table))

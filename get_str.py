# -*- coding:utf-8 -*-
"""
	获取一个字符串括号中的内容
"""
import re


def get_str(stri):
	result = re.findall(r'(?<=[(])[^\(\)]*(?=[)])',testStr)
	return result




if __name__ == '__main__':
	testStr = '(sdaf)sd((dsaf))((d)sd(s))'
	result = get_str(testStr)
	print result


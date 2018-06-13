# -*- coding:utf-8 -*-
"""
	写一个装饰器，打印方法foo() called ,打印其执行时间
"""
import time

def func_util(func):

	def wrapper(*args,**kwargs):
		print func.__name__+'() called'
		start_time = time.time()
		return_value = func(*args,**kwargs)
		end_time = time.time()
		print 'func costs:'+str(end_time-start_time)
		return return_value

	return wrapper


@func_util
def foo():
	pass

if __name__ == '__main__':
	foo()

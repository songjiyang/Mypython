# -*- coding:utf-8 -*-
"""
	写一个列表工具类，可以对列表进行去重，合并，求差，初始化的时候打印hello world，销毁的时候打印Good bye
"""

class List_util(object):
	"""列表工具类，可以对列表进行去重，合并，求差操作"""
	def __init__(self):
		super(List_util, self).__init__()
		print 'hello world'

	@classmethod
	def remove_repeat(cls, inlist):
		rsp_list = []
		for item in inlist:
			if item not in rsp_list:
				rsp_list.append(item)
		return rsp_list

	@classmethod
	def merge(cls, inlist1, inlist2):
		rsp_list = []
		for item in inlist1:
			rsp_list.append(item)
		for item in inlist2:
			rsp_list.append(item)
		rsp_list = cls.remove_repeat(rsp_list)
		return rsp_list

	@classmethod
	def sub(cls, inlist1, inlist2):
		rsp_list = []
		if  len(inlist1)>len(inlist2):
			max = inlist1
			min = inlist2
		else:
			max = inlist2
			min = inlist1
		for item in max:
			if item not in min:
				rsp_list.append(item)
		return rsp_list



if __name__ == '__main__':
	
	list1 = [2,56,52,34,5,2,4,5] 
	list2 = [2,3,4,5,6]

	print List_util.remove_repeat(list1)
	print List_util.merge(list1,list2)
	print List_util.sub(list1,list2)

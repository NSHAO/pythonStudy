#coding:utf-8
import time
class Sort():
	def __init__(self, list):
		self.description()
		self.name = raw_input("Please input a sort kind:")
		self.list = list
		print "This is a %s sort" % self.name

	def description(self):
		print "Now we will do number sort."
		print """we have mang ways to sort numbers.
		quick"""

	#排序主函数
	def sort(self):
		function_name = self.name + "_sort"
		l = list(self.list)
		func = getattr(self, function_name)
		starttime = time.clock()
		func(l, 0, len(l) - 1)
		endtime = time.clock()
		print "the sorted list:",
		print l
		print "sort spend time:%f seconds" % (endtime - starttime)

	#快速排序中间转换函数
	def middle_swap(self, list, first, last):
		cusor = list[first]
		i = first + 1
		j = last
		while True:
			while i <= last and list[i] <= cusor:
				i = i + 1
			while j > first and list[j] > cusor:
				j = j - 1
			if i < j:
				self.swap(list, i, j)
			else:
				break
		self.swap(list, first, j)
		return j

	#交换函数
	def swap(self, list, i, j):
		tmp = list[i]
		list[i] = list[j]
		list[j] = tmp
	
	#快速排序算法	
	def quick_sort(self, *args):
		list = args[0]
		first = args[1]
		last = args[2]
		if first >= last:
			return
		p = self.middle_swap(list, first, last)
		self.quick_sort(list, first, p - 1)
		self.quick_sort(list, p + 1, last)

	def merge_sort(self, *args):
		list = args[0]
		print ""
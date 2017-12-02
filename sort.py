#coding:utf-8
import time
import math
class Sort():
	def __init__(self, list):
		self.description()
		self.list = list

	def description(self):
		print "Now we will do number sort."
		print """we have mang ways to sort numbers.Choose one to sort your list!
		quick
		merge
		bubble
		selection
		insertion
		heap
		shell
		radix"""


######################################################################################


	#排序主函数
	def sort(self):
		while True:
			self.name = raw_input("Please input a sort kind:")
			function_name = self.name + "_sort"
			try:
				func = getattr(self, function_name)
			except Exception:
				print "Please input a usable sort arthimetic."
				continue
			break
		print "This is a %s sort" % self.name
		l = list(self.list)
		starttime = time.clock()
		func(l, 0, len(l) - 1)
		endtime = time.clock()
		print "the sorted list:",
		print l
		print "sort spend time:%f seconds" % (endtime - starttime)


	#交换函数
	def swap(self, list, i, j):
		tmp = list[i]
		list[i] = list[j]
		list[j] = tmp



######################################################################################


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


######################################################################################


	#归并排序
	def merge_sort(self, *args):
		list = args[0]
		first = args[1]
		last = args[2]
		if first >= last:
			return
		self.merge_sort(list, first, (first+last)/2)
		self.merge_sort(list, (first+last)/2+1, last)
		self.merge(list, first, (first+last)/2, last)

	#归并排序合并函数
	def merge(self, list, first, middle, last):
		newlist = list[:]
		i = 0
		j = 0
		k = first
		while True:
			if i >= middle - first + 1:
				# 多余
				# if j < last - middle:
				# 	for i in range(middle+1+j, last+1):
				# 		newlist[k] = list[i]
				# 		k = k + 1
				break
			elif j >= last - middle:
				if i < middle - first + 1:
					for a in range(first+i, middle+1):
						newlist[k] = list[a]
						k = k + 1
				break
			else:
				if list[first+i] <= list[middle+1+j]:
					newlist[k] = list[first+i]
					i = i + 1
					k = k + 1
				else:
					newlist[k] = list[middle+1+j]
					j = j + 1
					k = k + 1
		for i in range(first, last+1):
			list[i] = newlist[i]


######################################################################################


	#冒泡排序算法
	def bubble_sort(self, *args):
		list = args[0]
		for i in range(0, len(list)):
			for j in range(i, len(list)):
				if list[j] < list[i]:
					self.swap(list, i, j)


######################################################################################
	
	#选择排序算法
	def selection_sort(self, *args):
		list = args[0]
		for i in range(0, len(list) - 1):
			cusor = i
			for j in range(i, len(list)):
				if list[j] < list[cusor]:
					cusor = j
			self.swap(list, i, cusor)



######################################################################################

	
	#插入排序算法
	def insertion_sort(self, *args):
		list = args[0]
		for i in range(1, len(list)):
			cusor = list[i]
			for j in range(0, i)[::-1]:
				if list[j] >= cusor:
					list[j+1] = list[j]
					list[j] = cusor
				else:
					break



######################################################################################

	#堆排序算法
	def heap_sort(self, *args):
		list = args[0]
		self.create_min_heap(list)
		for i in range(0, len(list)-1):
			self.swap(list, 0, len(list)-1-i)
			if len(list)-1-i > 1:
				self.adjust_heap_node(list, 0, len(list)-1-i)

	#建立最小堆
	def create_min_heap(self, list):
		for i in range((len(list)+1)/2)[::-1]:
			self.adjust_heap_node(list, i, len(list))

	#调节堆节点
	def adjust_heap_node(self, list, i, length):
		
		k = i
		while 2*k + 1 < length:
			index = 2*k + 1
			if index + 1 < length:
				if list[index] < list[index+1]:
					index = index + 1
			if list[k] < list[index]:
				self.swap(list, k, index)
				k = index
			else:
				break
			


######################################################################################


	#希尔排序算法
	def shell_sort(self, *args):
		list = args[0]
		gap = len(list)/2
		while gap >= 1:
			print gap
			for i in range(gap, len(list)):
				cusor = list[i]
				j = i - gap
				while j >= 0:
					if list[j] > cusor:
						list[j+gap] = list[j]
						j = j - gap
					else:
						break
				list[j+gap] = cusor
			gap = gap/2
			


######################################################################################


	#基数排序算法
	def radix_sort(self, *args):
		list = args[0]
		digit = 1
		while self.middle_split(list, digit):
			digit = digit + 1

	#中间分桶函数
	def middle_split(self, list, digit):
		flag = 0
		k = 0
		partition_list = {}
		for i in range(len(list)):
			if list[i] >=0:
				number = int((list[i]/math.pow(10, digit-1))%10)
			else:
				number = -int((-list[i]/math.pow(10, digit-1))%10)
			#print digit, list[i], number
			if number == 0:
				flag = flag + 1
			if partition_list.has_key(number):
				partition_list[number].append(list[i])
			else:
				number_list = []
				number_list.append(list[i])
				partition_list[number] = number_list
		if flag == len(list):
			return False
		for i in range(-10,10):
			if partition_list.has_key(i):
				for j in range(len(partition_list[i])):
					list[k] = partition_list[i][j]
					k = k + 1
		return True
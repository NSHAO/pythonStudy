from sort import Sort
import datetime

while True:
	print "input exit to stop."
	input = raw_input("Please input a number list(like '[1,2,3]'):")
	if input == "exit":
		break
	else:
		try:
			input = eval(input)
		except Exception:
			print "not a number list.please input again!"
			continue
	if not isinstance(input, list):
		print "not a number list.please input again!"
		continue
	print "the original list:",
	print input
	Sort(input).sort() 
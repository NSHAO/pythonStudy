from sort import Sort
import datetime

while True:
	print("input exit to stop.")
	my_input = input("Please input a number list(like '[1,2,3]'):")
	if my_input == "exit":
		break
	else:
		try:
			my_input = eval(my_input)
		except Exception:
			print("not a number list.please input again!")
			continue
	if not isinstance(my_input, list):
		print("not a number list.please input again!")
		continue
	print("the original list:"),
	print(my_input)
	Sort(my_input).sort() 

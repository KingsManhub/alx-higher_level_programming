#!/bin/usr/python3
def safe_print_list(my_list=[], x=0):
	count = 0
	while True:
		try:
			if count < x:
				print(my_list[count], end="")
				index += 1
			else:
				print()
				return index
		except IndexError:
			print()
			return index

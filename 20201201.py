#import libs``
import math 
import adventlib as advl


def main():
	file = advl.openFile('20201201_data')
	data = advl.convertData(file)
	n1 = 0
	n2 = 0
	n3 = 0
	for v1 in data:
		for v2 in data:
			for v3 in data:
				if v1 != v2 != v3:
					if int(v1) + int(v2) + int(v3) == 2020:
						n1 = int(v1)
						n2 = int(v2)
						n3 = int(v3)
	print(n1)
	print(n2)
	print(n3)
	print(n1*n2*n3)
main()

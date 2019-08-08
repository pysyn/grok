def binarySearch(list, item):
	''' search the list for the target item
	    if found, return the index, i.e. the position in the my_list
	    otherwise, return None
	'''
	#vincent's code
	
	low=0
	high=len(list)-1
	
	while low <= high:
		mid=(low+high)//2
		if list[mid] > item:
			high=mid-1
		elif list[mid]==item:
			return mid
		else:
			low=mid+1
	return None

	




import unittest
class TestBinarySearch(unittest.TestCase):
	def test1(self):
		my_list = [1,3,5,7,9,11]
		self.assertEqual(binarySearch(my_list, 3), 1)
		self.assertEqual(binarySearch(my_list, 2), None)


if __name__ == '__main__':
	unittest.main()
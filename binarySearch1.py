def binarySearch(list, item):
	''' search the list for the target item
	    if found, return the index, i.e. the position in the my_list
	    otherwise, return None
	'''
	#vincent's code

	return None




import unittest
class TestBinarySearch(unittest.TestCase):
	def test1(self):
		my_list = [1,3,5,7,9,11]
		#self.assertEqual(binarySearch(my_list, 3), 1)
		self.assertEqual(binarySearch(my_list, 2), None)


if __name__ == '__main__':
	unittest.main()
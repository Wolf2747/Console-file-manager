def test_filters():
   new_numbers = list(filter(lambda x: x%2 == 0,[1,2,3,4,5,6,7,8,9,10]))
   assert new_numbers == [2,4,6,8,10]
def test_map():
   new_list = list(map(int,['1','2','3','4','5']))
   assert new_list == [1,2,3,4,5]
def test_sort():
   numbers = [1,25,-9,56,-128]
   numbers.sort()
   assert numbers == [-128,-9,1,25,56]
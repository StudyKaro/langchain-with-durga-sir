items = [0,1,2,3,4,5,6,7,8,9]
print(items[:])
copy_list = [0,2,8,10,20,30,40,50,60]
merge_list = {*copy_list,*items} //set
print(merge_list)

#*********01
my_list = []
print(my_list)
#********02
my_list.append([10,20,30,40])
print("after append:", my_list)
#**********03
my_list.insert(0, 15)
print("after insert:", my_list)
#*******04
my_list.extend([50,60,70])
print("after extend:",my_list)
#*********05
del my_list[4]
print(my_list)
#*********06
my_list = [15,10,20,30,40,50,60]
sorted_list = sorted(my_list)
print('sorted list in ascending order:', sorted_list)
#*********07
index_of_30 = my_list.index(30)
print("index of the value 30 in the list:",index_of_30)

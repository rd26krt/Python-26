import copy
#  == Operator

list1 = [1,2,3,4,5]
list2 = list1

print(list1)
print(list2)

list2[2] = 98

print(list1)
print(list2)
print("----------shallow copy----------------")
# shallow copy 

list3 = [1,2,3,4,5]
list4 = list3.copy()
print(list3)
print(list4)
list4[1] = 20
print(list3)
print(list4)
print("----------Shallow copy in nested list---------------")

list5 = [[1,2,3,4,5],[6,7,8,9,10]]
list6 = list5.copy()
list6[1][0] = 50
print(list5)
print(list6)



print("----------Deep copy---------------")
# Deep copy 

listt3 = [1,2,3,4,5]
listt4 = copy.deepcopy(listt3)
print(listt3)
print(listt4)
listt4[1] = 20
print(listt3)
print(listt4)
print("----------Deep copy in a nested list---------------")

listt5 = [[1,2,3,4,5],[6,7,8,9,10]]
listt6 = copy.deepcopy(listt5)
listt6[1][0] = 50
print(listt5)
print(listt6)
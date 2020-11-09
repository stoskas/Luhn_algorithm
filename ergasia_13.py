import numpy as np

vals1, vals2, vals3 = np.loadtxt('ergasia_13.txt')

list1 = vals1.tolist()
list2 = vals2.tolist()
list3 = vals3.tolist()

nested_list= []
nested_list.append(list1)
nested_list.append(list2)
nested_list.append(list3)
print(nested_list)

x = (nested_list[1][1]*nested_list[2][2])-(nested_list[1][2]*nested_list[2][1])
y = (nested_list[1][0]*nested_list[2][2])-(nested_list[1][2]*nested_list[2][0])
z = (nested_list[1][0]*nested_list[2][1])-(nested_list[1][1]*nested_list[2][0])

orizousa = (nested_list[0][0]*x) - (nested_list[0][1]*y) + (nested_list[0][2]*z)

print(orizousa)
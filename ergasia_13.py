import numpy as np

vals1, vals2, vals3 = np.loadtxt('ergasia_13.txt')

print(vals1,)
print(vals2)
print(vals3)

x = (vals2[1]*vals3[2])-(vals2[2]*vals3[1])
y = (vals2[0]*vals3[2])- (vals2[2]*vals3[0])
z = (vals2[0]*vals3[1])- (vals2[1]*vals3[0])

orizousa = (vals1[0]*x) - (vals1[1]*y) + (vals1[2]*z)

print(orizousa)
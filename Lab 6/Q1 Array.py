import numpy as np
from array import array

a = 0
s1 = [0,1,2,3,4,5,6,7,8,9,10,11,12]
s2 = []
s3 = []
s4 = []

for i in range(0,len(s1)): 
    a = int(s1[i]) + 2
    s2.append(a)
    
for i in range(0,len(s1)): 
    b = int(s1[i]) * 2
    s3.append(b)

for i in range(len(s1)):
    if i>7:
        i=i-10
    s4.append(i+2)


print(f"Add 2: {s2}")
print(f"Multiply by 2: {s3}")
print(f"Shift 2: {s4}")


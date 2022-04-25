s1=[]
a=input("Write a sentence: ").lower() 
num=0

b=a.split(" ") 

for i in b: 
    if i not in s1: 
        s1.append(i)
        num += 1
print(num)


a = 0
b = 1
cout = 0
n = int(input("Input a positive number: "))

while n <= 0: 
    print("Please input a number bigger than 0")
    n = int(input("Input a positive number: "))

print(f"The first {n} Fibonacci numbers:", end = " ")
while cout < n: 
    print(b, end = " ")
    next = a + b
    a = b
    b = next
    cout = cout + 1
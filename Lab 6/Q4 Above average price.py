
sum = 0
i = 0
n = int(input("How many items are on the menu? "))


food_list = []
price_list = []


for i in range(1, n+1): 
    food_input = input(f"Enter the {i} item: ")
    price_input = input(f"Enter the item {i} price: ")
    food_list.append(food_input)
    price_list.append(price_input)
    print()

print("\n")

for x in range(0,len(food_list)):
    i = x+1
    print(f"Item {i}: {food_list[x]}")
    print(f"Price of item {i}: {price_list[x]}")
    i += 1

print()
print("\n")
        
for i in range(0,n):
    price_list[i] = float(price_list[i])
    sum = sum + price_list[i]

avg = sum/n
print(f"Average price: {avg}")

for x in range(len(price_list)): 
    if price_list[x] >= avg: 
        print(f"Item(s) above average price: {food_list[x]}, {price_list[x]}")
        

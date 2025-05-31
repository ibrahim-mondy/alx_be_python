number = int(input("Enter a number to see its multiplication table:"))
for num in range(1, 10):
    result = number * num
    
    print(f"{num} * {number} = {result}")
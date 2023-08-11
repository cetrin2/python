#Задание 1

a = int(input())
arr = []
i = 0
zero_count = 0

while i < a:
    arr.append(int(input()))
    
    if arr[i] == 0:
        zero_count += 1
        
    i += 1
    
print("Entered numbers:")
print(*arr)
print("zero count ", zero_count)
print()

#Задание 2

max_num = 2 * 10 ** 9

print("Enter any number less then 2000000000")
n = int(input())
count = 0

if n <= max_num:
    for j in range(1, n + 1):
        if n % j == 0:
            count += 1
    

print("Found natural divisors:", count)
print()

#Задание 3

print("Enter A number")
print("Enter B number (must be more then A or equel)")
a = int(input())
b = int(input())
result = []

if a <= b:
    for i in range(a, b + 1):
        if i % 2 == 0:
            result.append(i)
            
print(*result)

#Задание 1

print("Enter the length and width of the rectangle (separator - space)")

a, b = map(float, input().split())
area = a * b
print("The area of the rectangle is", area)

perimetr = a + a + b + b
print("The perimeter of the rectangle is", perimetr)
print()

#Задание 2

print("Enter an integer five-digit number")
five_digit_num = int(input())

ones = five_digit_num % 10
tens = (five_digit_num % 100) // 10
hundreds = (five_digit_num % 1000) // 100
thousands = (five_digit_num // 1000) % 10
tenthousands = (five_digit_num % 100000) // 10000

result = tens ** ones * hundreds / (tenthousands - thousands)
print(result)

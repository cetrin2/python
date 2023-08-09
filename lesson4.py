#Задание 1

print("Enter the length of the sides of the triangle (separator - space)")

a, b, c = map(float, input().split())
area = a * b * c
print("The area of the triangle is", area)

perimetr = a + b + c
print("The perimeter of the triangle is", perimetr)
print()

#Задание 2

print("Enter an integer five-digit number")
five_digit_num = int(input())

#Находим числа по разряду
ones = five_digit_num % 10
tens = (five_digit_num % 100) // 10
hundreds = (five_digit_num % 1000) // 100
thousands = (five_digit_num // 1000) % 10
tenthousands = (five_digit_num % 100000) // 10000

#выполняем операции с числами
result = tens ** ones * hundreds / (tenthousands - thousands)
print(result)

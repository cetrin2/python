
#Задание 1

print("Enter any number")
number = int(input())

if number == 0:
    #Число равно нулю
    print("Number is zero")
elif number < 0 and number % 2 == 0:
    #Четное отрицательно
    print("Even negative number")
elif number > 0 and number % 2 == 0:
    #Четное положительное
    print("Even positive number")
elif number < 0 and number % 2 != 0:
    #Отрицательное нечетное
    print("Odd negative number")
else:
    #Положительное нечетное
    print("Odd positive number")
    
print()
    
#Задание 2

#Создаем массив гласных букв
vowels = ['a', 'e', 'i', 'o', 'u', 'y']

#Получаем строку от пользователя
print("Enter any word")
word = input()

count = 0

#Считаем буквы используя список из массива
for i in vowels:
    if word.count(i) == 0:
        print(i, "- False")
    else:
        print(i, word.count(i), sep=" - ")
        count += word.count(i)
        
#Считаем кол-во глассных и согласных
consonants_count = len(word) - count

print("Sum of vowels are :", count)
print("Sum of consonants are", consonants_count)
print()

#Задание 3

x = 5000

print("Enter Mike's money")
mike = float(input())

print("Enter Ivan's money")
ivan = float(input())

#У Майка хватает и у Ивана хватает
if mike >= x and ivan >= x:
    print(2)
    
#Майк может вложиться
if mike >= x:
    print("Mike")
    
#Иван может вложиться
if ivan >= x:
    print("Ivan")
    
#У Майка не хватает и у Ивана не хватает, но в сумме хватает
if mike < x and ivan < x and ivan + mike >= x:
    print(1)
    
#Даже в сумме не хватает
if mike + ivan < x:
    print(0)

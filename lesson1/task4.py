prompted_number_string = input('Введите целое положительное число: ')
greatest_number = -1
i = 0

while i < len(prompted_number_string):
    number = int(prompted_number_string[i])
    if greatest_number < number:
        greatest_number = number
    i += 1

print('Наибольшая цифра в числе:', greatest_number)

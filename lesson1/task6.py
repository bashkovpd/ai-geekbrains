first_day_result = float(input('Введите результат спортсмена в первый день: '))
target_distance = float(input('Введите финальную дистаницю: '))
current_day_result = first_day_result
day = 1

while current_day_result < target_distance:
    current_day_result = current_day_result * 1.1
    day += 1

print('На {} день спортсмен достиг резултата - не менее {}'.format(day, target_distance))
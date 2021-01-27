revenue = float(input('Введите выручку фирмы: '))
costs = float(input('Введите издержки фирмы: '))

if revenue > costs:
    print('Фирма приносит прибыль')
    print('Рентабильность выручки фирмы:', revenue / costs * 100)

    employees_count = int(input('Введите количество сотрудников фирмы: '))

    print('Прибыль фирмы в расчёте на одного сотрудника: ', revenue / costs / employees_count * 100)
else:
    print('Фирма несёт убытки')

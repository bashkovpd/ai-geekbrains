seconds_in_hour = 60 ** 2
seconds_in_minute = 60

prompted_seconds = int(input('Введите число секунд: '))
hours = prompted_seconds // seconds_in_hour
minutes = (prompted_seconds - hours * seconds_in_hour) // seconds_in_minute
seconds = prompted_seconds - hours * seconds_in_hour - minutes * seconds_in_minute

print("{:0>2}:{:0>2}:{:0>2}".format(hours, minutes, seconds))
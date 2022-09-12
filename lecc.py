# n = int(input('ввидите день недели: '))
# if (n == 6 or n == 7):
#     print('выходной')
# else:
#     print('нет')






# x = int(input('ввидите кардинату х: '))
# y = int(input('ввидите кардинату y: '))
# if x > 0 and y > 0:
#     print('1')
# if x < 0 and y > 0:
#     print('2')
# if x < 0 and y < 0:
#     print('3')
# if x > 0 and y < 0:
#     print('4')





# n = int(input('ввидите номер четверти: '))
# if n == 1:
#      print('x > 0 и y > 0')
# elif n == 2:
#      print('x < 0 и y > 0')
# elif n == 3:
#      print('x < 0 и y < 0')
# elif n == 4:
#      print('x > 0 и y < 0')





print('Enter coordinates point А:')
x_A = float(input('X: '))
y_A = float(input('Y: '))
print("Enter coordinates point B:")
x_B = float(input('X: '))
y_B = float(input('Y: '))

from math import sqrt
print('Distance between A and B: ',round(sqrt((x_A - x_B)**2 + (y_A - y_B)**2), 2))

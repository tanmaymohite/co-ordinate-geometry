#distance formula program
from math import sqrt

print('-----------------------------------------------')
print('                 Distance formula')
print('-----------------------------------------------')
print('      d(x,y) = sqrt(x2-x1)^2+(y2-y1)^2)')
print('-----------------------------------------------')

x1 = input('Enter the value of x1: ')
x1 = int(x1)

x2 = input('Enter the value of x2: ')
x2 = int(x2)

y1 = input('Enter the value of y1: ')
y1 = int(y1)

y2 = input('Enter the value of y2: ')
y2 = int(y2)

x = (x2-x1)**2
y = (y2-y1)**2
d= sqrt( x + y)
print('\nd(a,b) = '+str(d))
print('-----------------------------------------------')
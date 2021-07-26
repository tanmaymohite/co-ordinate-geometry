#section formula program

print('-----------------------------------------------')
print('                 Section formula')
print('-----------------------------------------------')
print('           mX2+nX1/m+n,mY2+nY1/m+n')
print('-----------------------------------------------')

x1=input('Enter the value of x1: ')
x1=int(x1)

x2=input('Enter the value of x2: ')
x2=int(x2)

y1=input('Enter the value of y1: ')
y1=int(y1)

y2=input('Enter the value of y2: ')
y2=int(y2)

m=input('Enter the value of m: ')
m=int(m)

n=input('Enter the value of n: ')
n=int(n)

x=((m * x2) + (n * x1))/(m + n)
y=((m * y2) + (n * y1))/(m + n)

print('\nx,y= '+str(x)+' , '+str(y))

from math import sqrt
# calculate your BMI
print('------------calculate your BMI------------')

a = input('Enter your weight [kg] :  ')
a = float(a)

b = input('Enter your height[IN CM] : ')
b = float(b)

c = b*b
c = float(c)

bmi = a / c

print(bmi)

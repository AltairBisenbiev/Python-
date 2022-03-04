import math
s = int(input("Input number of sides: "))
l = int(input("Input the length of a side: "))
p = s*l
a = l/(2*(math.tan(math.pi/s)))
area = (p*a)/2
print("The are of polygon is: " + str(int(area)))



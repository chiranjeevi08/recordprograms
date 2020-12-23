from math import pi,tan

def square(side):
	area=side*4
	return area
def circle(radius):
	
	area=pi*radius**2
	return area
def polygon(sides,length):
	
	area=sides*(length**2)/(4**tan(pi/sides))
	return area


print("To Calculate Area OF Square Enter 1:")
print("To Calculate Area OF circle Enter 2:")
print("To Calculate Area OF Polygon Enter 3:")
opt=int(input("Enter Your Choice:"))
if(opt==1):
	side=int(input("Enter Length OF The Side In Centimeter:"))
	area=square(side)
	print("Area Of The Square Is",area,"CM")
elif(opt==2):
	radius=int(input("Enter Radius Of The Circle:"))
	
	area=circle(radius)
	print("Area Of Rectangle Is",area,"CM")
elif(opt==3):
	side=int(input("Enter Number Of Sides:"))
	length=int(input("Enter Length Of The Side In Centimeter:"))
	area=polygon(side,length)
	print("Arer Of polygon Is",area,"CM")
else:
	print("Enter A Valid Option")




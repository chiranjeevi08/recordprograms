

def square(side):
	area=side*4
	return area
def circle(radius):
	area=3.14*radius**2
	return area
def triangle(length,breath):
	area=0.5*length*breath
	return area


print("To Calculate Area OF Square Enter 1:")
print("To Calculate Area OF circle Enter 2:")
print("To Calculate Area OF Trinagle Enter 3:")
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
	length=int(input("Enter Length Of The Triangle In Centimeter:"))
	breath=int(input("Enter Breath Of The Triangle In Centimeter:"))
	area=triangle(length,breath)
	print("Arer Of Triangle Is",area)
else:
	print("Enter A Valid Option")




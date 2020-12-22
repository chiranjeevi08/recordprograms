import currency
print("To Convert Rupees Into Dollers Enter 1 ")
print("To Convert Dollers Into Rupees Enter 2")
opt=int(input("Enter Your Option:"))
if(opt==1):
	amount=int(input("Enter Amount:"))
	price=currency.rupees(amount)
	print(price,"dollers")
elif(opt==2):
	amount=int(input("Enter Amount:"))
	price=currency.dollers(amount)
	print(price,"rupees")
else:
	print("Enter Valid Option")

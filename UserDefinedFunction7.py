#There is diagram of this Program

def Calculations(No1,No2):
	Mult = No1 * No2
	Div = No1 / No2

	return Mult,Div

def main():
	Value1 = int(input("Enter First Number :"))
	Value2 = int(input("Enter Second Number :"))

	Ret1 , Ret2 = Calculations(Value1,Value2)
	print("Multiplication is : ",Ret1)
	print("Division is :",Ret2) 

	

if __name__ == "__main__":
	main()
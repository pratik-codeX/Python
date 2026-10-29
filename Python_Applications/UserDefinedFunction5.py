

#Accept : Multiple Parameter
#Return : Multiple Value

def marvellous(Value1,Value2):
	print("Inside Marvellous :",Value1,Value2)
	return 21,51
	
def main():
	Ret1,Ret2 = marvellous(10,20)
	print("Return values are :",Ret1,Ret2)

if __name__ == "__main__":
	main()

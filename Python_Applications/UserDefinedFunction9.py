#nested/Inner funtions

def BigBazar():
	print("Inside BigBazar")

	def Amul():
		print("Inside Amul Icecream Parlor")

	Amul()
	Amul()

def main():
	BigBazar()			#Allowed
	
if __name__ == "__main__":
	main()

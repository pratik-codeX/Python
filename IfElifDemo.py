'''
Algorith:

'''
#print("-"*40)
print("-------------------------------------------------")      #industrial banner
print("-------------Ticket Pricing Software-------------")
print("-------------------------------------------------")

print("Enter Your Age : ")
Age = int(input())

if (Age <= 5):
    print("Free Entry")
elif(Age > 5 and Age <= 18):
    print("Ticket price : 900")
elif(Age > 18 and Age <= 40):
    print("Ticket price is : 1200")
else:
    print("Ticket price is 500")
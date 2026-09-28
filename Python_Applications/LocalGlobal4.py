no = 11         

def Display():
    global no
    no = 21
    print("from Display",no)

print("Before",no)
Display()
print("After",no)
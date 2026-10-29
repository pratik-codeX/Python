embedding = {
    0 : [0.0,0.0,0.0],  # adding
    1 : [0.2,0.4,0.1],  # food
    2 : [0.3,0.1,0.5],  # was
    3 : [0.8,0.7,0.9],  # good
    4 : [0.1,0.2,0.9],  # bad
    5 : [0.9,0.3,0.3]   # not
}

sequence = [1,2,5,3]

print("Sequence for 'food was not good' is :", sequence)

for token in sequence:
    print("Token :",token)
    print("Vector : ",embedding[token])
    print("------------------------------")
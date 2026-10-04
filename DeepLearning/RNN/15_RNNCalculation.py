# ht = tanh(Wx * Xt + Wh * ht - 1 + b)

# xt        Current input
# Wx      Weight of current input
# Wh        Weight of previous hidden state 
# b             Bias
# ht -1     previous hidden state
# tanh      Activation function (-1 to 1)
# ht            New hidden state

import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))     #eulers constant


def MarvellousRNNPredications():
    print("Calculation of RNN : ")

    # food was not good
    inputs = [1,2,5,3]

    hidden_state = 0

    # RNN parameters
    Wx = 0.5
    Wh = 0.0
    bias = 0.1

    # RNN Calculation
    for time_step , x in enumerate(inputs):
        previous_hidden_state = hidden_state
        
        weighted_input = Wx * x
        
        weighted_memory = Wh * previous_hidden_state
        
        total = weighted_input + weighted_memory + bias
        
        hidden_state = np.tanh(total)
        
        print("Time Step : ",time_step + 1)
        print("Input : ", x)
        print("Hidden state :",hidden_state)
        
        print("--"*30)
    
    # Step 2 :  Final HIdden state
    print("final Hidden state :",hidden_state)
    
    # Step 3 : Output Layer
    # output = Wy * FinalHiddenstate + output Bias
    
    Wy = 1.0
    output_bias = 0.0
    
    output = (Wy * hidden_state ) + output_bias
    
    print("Raw output : ",output)

    
def main():
    MarvellousRNNPredications()

if __name__ == "__main__":
    main()

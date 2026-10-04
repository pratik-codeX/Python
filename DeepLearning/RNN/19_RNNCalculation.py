import numpy as np

from tensorflow.keras.preprocessing .text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, SimpleRNN, Dense

# Step 1 : Load the Data
train_sentenses = [
    "food was good",
    "food was bad",
    "food was excellent",
    "food was terrible",
    "service was good",
    "service was bad",
    "service was excellent",
    "service was terrible",
     "ambiance was good",
    "ambiance was bad",
    "ambiance was excellent",
    "ambiance was terrible"
]

train_labels = [
    1,
    0,
    1,
    0,
    1,
    0,
    1,
    0,
    1,
    0,
    1,
    0
]

# Step 2 : Tokenisation
tokenizer = Tokenizer(oov_token = "<OOV>")

tokenizer.fit_on_texts(train_sentenses)

# Step 3 : Convert training data into sequence 

train_sequence = tokenizer.texts_to_sequences(train_sentenses)

print("Training Sequences : ")

for sentense, sequance in zip(train_sentenses,train_sequence):
    print(sentense ," -> ",sequance)
    
# step 4 : Apply padding

max_length = 4

X_train = pad_sequences(

    train_sequence,
    maxlen = max_length,
    padding = "pre"
)

Y_train = np.array(train_labels)

print("Padded training data ")
print(X_train)

print("Training Labels ")
print(Y_train)

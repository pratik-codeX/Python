import numpy as np

from tensorflow.keras.preprocessing .text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences   #method
from tensorflow.keras.models import Sequential  #class
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

# Step 5 : Calculate Vocubalor size 

vocab_size = len(tokenizer.word_index) + 1

print("Vocubalor size is : ",vocab_size)

# Step  6 : build RNN model

model = Sequential()

model.add(
    Embedding(
        input_dim = vocab_size,
        output_dim = 8,
        input_length = max_length
    )
)

model.add(
    SimpleRNN(
        units = 8 ,
        activation = "tanh"
    )
)

model.add(
    Dense(
        units = 1,
        activation = "sigmoid"
    )
)

# Step 7  : Compile the model

model.compile(
    optimizer = "adam",
    loss = "binary_crossentropy",
    metrics = ["accuracy"]
)

# Step 8 : Display model

model.build(
    input_shape = (None, max_length)
)

print("Model Architecture ")
model.summary()

# step 9 : Train the model

history = model.fit(
    X_train,
    Y_train,
    epochs = 100,
    verbose = 1
)

print("Model Training completed")

# Step 10 : Create Unseed data

test_sentences = [
    "service was amazing",
    "service was horrible",
    "experience was excellent",
    "experiance was terrible"
]

# Step 11 : Convert text to sequence

test_sequences = tokenizer.texts_to_sequences(test_sentences)

X_test = pad_sequences(
    test_sequences,
    maxlen = max_length,
    padding = "pre"
)

# Step 12 : Predict the sentiment

for text , sequence, padded in zip(test_sentences,test_sequences,X_test):
    input_data = np.array([padded])
    
    predication = model.predict(input_data,verbose = 0)
    
    probability = float(predication[0][0])
    
    print("Setance : ",text)
    print("Sequence : ",sequence)
    print("Padded sequence : ",padded)
    print("Prediction ",probability)
    
    if predication >= 0.5:
        print("Positive ")
    else:
        print("Negative")

##########################################################
# Step 1 : Load the Libraries and Modules
##########################################################

from tensorflow.keras.datasets import imdb
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.preprocessing.sequence import pad_sequences

#########################################################
# Step 2 : Configuration of Values 
#########################################################

VOCAB_SIZE = 10000  # consider most frequent 10000 unique words
MAX_LENGTH = 200    # consider maximum 200 words in review

#########################################################
#   Step 3 : Load the IMDB dataset (Internet movie database)
#########################################################

print("-"*40)
print("Movie Review Sentiment Analysis using LSTM")
print("-"*40)

print("Loading the dataset...")

(X_train,Y_train),(X_test, Y_test) = imdb.load_data( num_words = VOCAB_SIZE )

print("IMDB dataset loaded succesfully")

print("Number of training reviews : ",len(X_train))     
print("Number of testing reviews : ",len(X_test))

#########################################################
#   X_train     : Reviews user for training
#   Y_train     : Actual Sentiments of training
#   X_test      : Reviews used for testing
#   Y_test      : Actual sentiments of testing
#
#   Sentiments : 
#   0 -> Negative Sentiments
#   1 -> Positive Sentiments
#########################################################

#########################################################
#   Step 4 :  load the Dictonary
#########################################################

word_index = imdb.get_word_index()

# Dictonary contains mapping of word and its corresponding number
# Drishyam is good movie        -> (20  58  78  43)
# 20            -> drishyam
# 58            -> is
# 78            -> good
# 43            -> movie

#########################################################
#  Step 5 : Create reverse Dictonary
#########################################################

reverse_word_index = {}

for word , index in word_index.items():
    reverse_word_index[index+3] = word
    
#########################################################
#   Step 6 : Function to decode the review (number to word)
#########################################################

def DecodeReview(encoded_review):
    words = [] 
    
    for number in encoded_review:
        if number >= 3:     # ignore first 3
            word = reverse_word_index.get(number , "?")
            words.append(word)
            
    return " ".join(words)      #join the list of words
    
#########################################################
#   Step 7 : Display Sample Reviews
#########################################################

print("-"*40)
print("--------------- Sample Reviews ---------------")
print("-"*40)

for i in range(3,7) : 
    
    reveiw = DecodeReview(X_train[i])
   
    print("-"*40)
    print("Review number : ", i + 1)
    print("Review : ")
    print(reveiw)
    
    print("-"*40)
    
    if Y_train[i] == 1:
        print("Sentimate : Positive")
    else:
        print("Sentimate : Negative")
        
#########################################################
#   Step 8 : Padding
#########################################################

X_train_padded = pad_sequences(
        X_train,
        maxlen = MAX_LENGTH
)

X_test_padded = pad_sequences(
        X_test,
        maxlen = MAX_LENGTH
)
    
print("Training data shape : ",X_train_padded.shape)
print("Testing data shape : ",X_test_padded.shape)

#########################################################
#   Step 9 : Create LSTM Model
#########################################################

model = Sequential()

model.add(
        Embedding(
                input_dim = VOCAB_SIZE,
                output_dim=32           # Each word is represented in 32 values (Each token have 32 vectors)
        )
)

model.add(
        LSTM(
                        units = 64        # size of LSTM hidden state
                        
        )
)

model.add(
        Dense(
                units = 1,          # one output
                activation = "sigmoid"      # used to produce probability
        )
)

# Project Architecture
# Review -> Embedding -> LSTM -> Sigmoid -> Positive / Negative

#########################################################
#   Step 10 : Compile the model
#########################################################

model.compile(
        optimizer = "adam",                               # algorithm to update the weights
        loss = "binary_crossentropy",          # loss function
        metrics = ["accuracy"]                           # Measure Classification accuracy
)

#########################################################
#   Step 11 : Train the model
#########################################################

print("Model Training")

model.fit(
        X_train_padded,        # Input training reviews
        Y_train,                         # Actual sentiment labels
        epochs = 3,                # Complete dataset gets process 3 times
        batch_size = 64,          # Process 64 reviews in one batch                
        validation_split = 0.2  #use 20% training for validation
)

print("Model training gets completed")
#########################################################
#   Step 12 : Evaluate the model
#########################################################

accuracy = model.evaluate(
        X_test_padded,              #   Testing Reviews
        Y_test,                               #     Actual testing labels
        verbose = 0                      #      Don't Display the process bar
)

print("Testing Accuracy : ", accuracy)

#########################################################
#   Step 13 : Predict the review
#########################################################

TEST_REVIEW_NUMBER = 0

original_review = X_test[TEST_REVIEW_NUMBER]
decoded_review = DecodeReview(original_review)

print("Review given to the model : ")
print(decoded_review)

#########################################################
#   Step 14 : Get the Actual sentiment
#########################################################

actual_value = Y_test[TEST_REVIEW_NUMBER]

if actual_value == 1:
    actual_sentiment = "POSITIVE"
else:
    actual_sentiment = "Negative"
    
print("Actual Sentiment : ",actual_sentiment)

#########################################################
#   Step 15 : Predict the Sentiment
#########################################################

review_for_prediction = X_test_padded[TEST_REVIEW_NUMBER + 1]

predication = model.predict(
        review_for_prediction.reshape(1,MAX_LENGTH),
        verbose = 0
)

probability = predication[0][0]

if probability >=0.5:
    predicted_sentiment = "POSITIVE"
else:
    predicted_sentiment = "NEGATIVE"
    

print("-"*40)
print("Final Result")

print("Prediction Probability : ",probability)
print("Actual Sentiment : ",actual_sentiment)
print("Predicted Sentiment : ",predicted_sentiment)     

print("-"*40)

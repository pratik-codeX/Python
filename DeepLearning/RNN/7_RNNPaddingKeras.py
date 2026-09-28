from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

sentenses = [
    "food was good",
    "food was bad",
    "food was not good"
]

tokenizer = Tokenizer()

tokenizer.fit_on_texts(sentenses)

sequences = tokenizer.texts_to_sequences(sentenses)

print("Original Sequences ")

for sequence in sequences:
    print(sequence,"Length : ",len(sequence))

print("All sequences are of deffirent lengths")

max_length = 4

padded_sentenses = pad_sequences(
    sequences,
    maxlen = max_length,
    padding = "pre"
)

for sentece , sequence, padded in zip(sentenses, sequences,padded_sentenses):
    print("sentence : ",sentece)
    print("Original sequance : ",sequence)
    print("Padded Sequence : ",padded)

    print("----------------------------------------------")
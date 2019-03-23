import pandas as pd
import numpy as np

from keras.layers import Lambda
from keras import backend as K

from keras.models import Model, Sequential
from keras.layers import Input, LSTM, Dense

from keras.preprocessing.text import text_to_word_sequence
from keras.preprocessing.text import Tokenizer

# Read technology toolkits data from csv file into panda table



# Model to get useful toolkites to use based on technologies familiar

# Model returns a vector of values, each for a toolkit/library and the value indicating the usefulness

# Define regression model
def tech_regression_model():
    # Create model
    model = Sequential()
    model.add(Dense(7, activation='relu', input_shape=()))
    model.add(Dense(50, activation='relu'))
    model.add(Dense(21))
    
    # Compile model
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

# User input generalization
    
# Categories
cat_docs = [
    "environment",
    "education",
    "social",
    "agriculture",
    "urban"
]

tok = Tokenizer()
tok.fit_on_texts(cat_docs)

print(tok.word_counts)
print(tok.document_count)
print(tok.word_index)
print(tok.word_docs)

# Technologies
tech_docs = [
    "python",
    "java",
    "javascipt",
    "website",
    "android",
    "ios",
    "vr"
]

tok2 = Tokenizer()
tok2.fit_on_texts(tech_docs)

print(tok2.word_counts)
print(tok2.document_count)
print(tok2.word_index)
print(tok2.word_docs)

# Get category input
category_string = input("Input hackathon category:")
category_arr = text_to_word_sequence(category_string)

# Encode new categories (string -> int)
category = tok.texts_to_matrix(category_arr, mode='count')
print(category)

# Get familiar techologies input
tech_string = input("Input familiar technologies, programming languages .etc")
tech_arr = text_to_word_sequence(tech_string)

# Get technology input
tech = tok2.texts_to_matrix(tech_arr, mode='count')
print(tech)

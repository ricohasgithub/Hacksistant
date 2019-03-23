import pandas as pd
import numpy as np

from keras.layers import Lambda
from keras import backend as K

from keras.models import Model, Sequential
from keras.layers import Input, LSTM, Dense

from keras.preprocessing.text import text_to_word_sequence
from keras.preprocessing.text import Tokenizer


# Read technology toolkits data from csv file into panda table
tech_toolkits_data = pd.read_csv("datasets/tech_toolkits.csv")
print(tech_toolkits_data.head())
print(tech_toolkits_data.shape)
print(tech_toolkits_data.describe())

tech_toolkits_data_columns = tech_toolkits_data.columns

# Toolkit name
tech_toolkit_names = tech_toolkits_data[tech_toolkits_data_columns[0]]
print(tech_toolkit_names)

# Toolkit int value
tech_toolkit_vals = tech_toolkits_data[tech_toolkits_data_columns[1]]
print(tech_toolkit_vals)

# Associated language of toolkit (in int value of language)
tech_toolkit_asclan = tech_toolkits_data[tech_toolkits_data_columns[2]]
print(tech_toolkit_asclan)

# Type of program (e.g., app, website, mobile .etc)
tech_toolkit_type = tech_toolkits_data[tech_toolkits_data_columns[3]]
print(tech_toolkit_type)


# Read training data with results
tech_toolkits_train = pd.read_csv("datasets/tech_toolkit_train.csv")

tech_toolkits_train_columns = tech_toolkits_train.columns

# Type of desired program
tech_toolkits_train_type = tech_toolkits_train[tech_toolkits_train_columns[0]]
print(tech_toolkits_train_type)

# Language predicter data
tech_toolkits_train_lan = tech_toolkits_train[tech_toolkits_train_columns[1:9]]
print(tech_toolkits_train_lan)

# Toolkit use target data
tech_toolkits_train_tar = tech_toolkits_train[tech_toolkits_train_columns[9:19]]
print(tech_toolkits_train_tar)


# Model to get useful toolkites to use based on technologies familiar

# Model returns a vector of values, each for a toolkit/library and the value indicating the usefulness

# Define regression model
def tech_regression_model():
    # Create model
    model = Sequential()
    model.add(Dense(9, activation='relu', input_shape=()))
    model.add(Dense(27, activation='relu'))
    model.add(Dense(8))
    
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
    "javascript",
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

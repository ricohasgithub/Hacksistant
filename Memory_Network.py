from keras.layers import Lambda
from keras import backend as K

from keras.models import Model, Sequential
from keras.layers import Input, LSTM, Dense

from keras.preprocessing.text import text_to_word_sequence
from keras.preprocessing.text import Tokenizer

# Model to get useful toolkites to use based on model

# Define regression model
def regression_model():
    # Create model
    model = Sequential()
    model.add(Dense(7, activation='relu', input_shape=()))
    model.add(Dense(50, activation='relu'))
    model.add(Dense(25))
    
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



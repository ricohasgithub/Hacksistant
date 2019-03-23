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


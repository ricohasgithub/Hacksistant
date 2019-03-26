
import numpy as np
import pandas as pd

from keras.preprocessing.text import text_to_word_sequence
from keras.preprocessing.text import Tokenizer

from firebase import firebase
from keras.models import load_model

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

# Program Type
tprogram_docs = [
        "app",
        "website",
        "mobile"
]

tok3 = Tokenizer()
tok3.fit_on_texts(tprogram_docs)

print(tok3.word_counts)
print(tok3.document_count)
print(tok3.word_index)
print(tok3.word_docs)

# Method used to decode and decide best toolkit use
def get_results (pred):
    _max_ = ""
    max_val = 0
    for i in range(len(pred)):
        for j in range(len(pred[i])):
            if pred[i][j] > max_val:
                max_val = pred[i][j]
                _max_ = tech_toolkits_data.iloc[j,0]
    return "Recommended toolkit for use: " + _max_

# Method used to parse the JSON String
def parse_json (json):
    json_arr = json.split()
    print(json_arr[-1])
    return json_arr[-1]

# Firebase GET and POST info
firebase = firebase.FirebaseApplication('https://last-second-hack-128ce.firebaseio.com', None)

pretrained_model = load_model('toolkit_model.h5')
#name_pretrained_model = load_model('name_gen_model.h5')

print("Models Loaded Successfully")

#input_name = name_pretrained_model.predict_on_batch("iCare")

#print(input_name)

while True:
    
    # Get whether to pull or not
    done = firebase.get('/response', 'done')
    print(done)
    
    # User has finished entering commands, get new update and feed into network and post
    if done:
        # Get three query fields
        topic_json = firebase.get('/response', 'topic')
        topic = parse_json(topic_json)
        category_arr = text_to_word_sequence(topic)
        category = tok.texts_to_matrix(category_arr, mode='count')
        
        language_json = firebase.get('/response', 'language')
        language = parse_json(language_json)
        tech_arr = text_to_word_sequence(language)
        tech = tok2.texts_to_matrix(tech_arr, mode='count')
        
        platform_json = firebase.get('/response', 'platform')
        platform = parse_json(platform_json)
        tprogram_arr = text_to_word_sequence(platform)
        tprogram = tok3.texts_to_matrix(tprogram_arr, mode='count')
        
        # Get Predictor
        input_pred = np.zeros((1,9))

        input_type_index = 0

        for i in range(len(tprogram)):
            for j in range(len(tprogram[i])):
                input_type_index += 1
                if tprogram[i][j] == 1:
                    break

        input_pred[0][0] = input_type_index
    
        for i in range(len(tech)):
             count = 1
             for j in range(len(tech[i])):
                input_pred[0][count] = tech[i][j]
                count += 1
        
        print(input_pred)
        
        # Run model and get output
        input_eval = pretrained_model.predict_on_batch(input_pred)
        
        # Get hackathon name
        
        
        response = get_results(input_eval)
        
        #result = firebase.post('/output/answer', response,{'print': 'silent'}, {'X_FANCY_HEADER': 'VERY FANCY'})
        #print(result)

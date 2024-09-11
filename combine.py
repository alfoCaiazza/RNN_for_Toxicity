import pandas as pd
import tensorflow as tf
from tensorflow.keras.layers import TextVectorization
from transcribe import get_audio

MAX_FEATURES = 200000

model = tf.keras.models.load_model('toxicity_analyzer.h5')
vectorizer = TextVectorization(max_tokens=MAX_FEATURES, output_sequence_length=1800, output_mode='int')

#Loading the dataset
df = pd.read_csv('train.csv')
X = df['comment_text']

vectorizer.adapt(X.values)

#Automizing vectorization
def score_comment(comment):
    vectorized_comment = vectorizer([comment]) #Vectorize comment
    result = model.predict(vectorized_comment) #Predict toxicity

    text = ''
    for idx, col in enumerate(df.columns[2:]):
        text += '{} : {}\n'.format(col, result[0][idx] > 0.5) #Unpacking the result

    return text

speech_to_text = get_audio()
print(speech_to_text)
values = score_comment(speech_to_text)
print('Values: ', values)
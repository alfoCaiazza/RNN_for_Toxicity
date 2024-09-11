import string
from nltk.corpus import stopwords

stopwords_list = stopwords.words('english')
paths = ['toxic_file.txt','severe_toxic_file.txt','treath_file.txt','obscene_file.txt','insult_file.txt','identity_hate_file.txt']

#Cleaning the data
def text_cleaning(file, stopwords):
    text = file.read()

    # Removing punctation
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator)
    
    # Removing special char
    text = ''.join(char for char in text if char.isalnum() or char.isspace())

    # Lowercase
    text = text.lower()
    
    # Removing stopword
    words = text.split()
    cleaned_text = ' '.join(word for word in words if word.lower() not in stopwords)
    
    return cleaned_text

for path in paths:
    print(f'Updating {path} file')
    with open(path, "r", encoding="utf-8") as file:
        cleaned_text = text_cleaning(file, stopwords_list)

    with open(path, "w", encoding="utf-8") as file:
        file.write(cleaned_text)
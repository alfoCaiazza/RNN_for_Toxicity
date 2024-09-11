import pandas as pd

#Open dataset
df = pd.read_csv('train.csv')

#Getting the labels
labels = ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']

#Creating a file for each label:
toxic_file = open('toxic_file.txt', 'a', encoding="utf-8")
severe_toxic_file = open('severe_toxic_file.txt', 'a', encoding="utf-8")
obscene_file = open('obscene_file.txt', 'a', encoding="utf-8")
threat_file = open('treath_file.txt', 'a', encoding="utf-8")
insult_file = open('insult_file.txt', 'a', encoding="utf-8")
identity_hate_file = open('identity_hate_file.txt', 'a', encoding="utf-8")


def create_label_files(df, labels):
    #Iterating labels
    for index, row in df.iterrows():
        print(f'Processing row num {index}')
        for label in labels:

            if row[label] == 1:
                if label == 'toxic':
                    toxic_file.write(row['comment_text'])
                elif label == 'severe_toxic':
                    severe_toxic_file.write(row['comment_text'])
                elif label == 'obscene':
                    obscene_file.write(row['comment_text'])
                elif label == 'threat':
                    threat_file.write(row['comment_text'])
                elif label == 'insult':
                    insult_file.write(row['comment_text'])
                elif label == 'identity_hate':
                    identity_hate_file.write(row['comment_text'])

create_label_files(df, labels)

toxic_file.close()
severe_toxic_file.close()
obscene_file.close()
threat_file.close()
insult_file.close()
identity_hate_file.close()
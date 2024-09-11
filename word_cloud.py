from wordcloud import WordCloud
import matplotlib.pyplot as plt

#Files list
paths = ['toxic_file.txt', 'severe_toxic_file.txt', 'obscene_file.txt', 'treath_file.txt', 'insult_file.txt', 'identity_hate_file.txt']
labels = ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']

for index, path in enumerate(paths):
    print(path)
    # Creating a wordcloud for each label
    wordcloud_text = open(path, 'r', encoding="utf-8").read()

    wordcloud = WordCloud(width=800, height=400, background_color='white', collocations=False).generate(wordcloud_text)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.savefig(f"{labels[index]}.png", format="png", bbox_inches='tight', pad_inches=0)

import pandas as pd
import nltk
# load data
data = pd.read_csv('financial_news_data.csv')
# clean data
data = data.dropna()
data['text'] = data['text'].apply(lambda x: x.lower()) # convert to lowercase
data['text'] = data['text'].apply(lambda x: nltk.word_tokenize(x)) # tokenize
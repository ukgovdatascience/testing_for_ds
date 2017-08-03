import nltk
from nltk.corpus import stopwords

def extract_words(text):
    '''Excludes stop words'''
    word_list = nltk.word_tokenize(text)
    filtered_words = [word for word in word_list
                      if word not in stopwords.words('english')]
    return filtered_words

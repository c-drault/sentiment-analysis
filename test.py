#!/usr/bin/env python
# coding: utf-8

# In[14]:


import sys


def remove_punctuation(text):
    final = "".join(u for u in text if u not in ("?", ".", ";", ":",  "!",'"'))
    return final

def sentiment_analysis(sentence):
    X_new = vectorizer.transform(sentence)
    result = lr.predict(X_new)[0]
    if result > 0:
        print("Hmmmm... your sentence is positive")
    if result < 0:
        print("Hmmmm... your sentence is negative")
    if result == 0:
        print("Hmmmm... your sentence is neutral")

    return result


if __name__ == "__main__":
    
    import pandas as pd
    import nltk
    from nltk.corpus import stopwords
    from nltk.stem import SnowballStemmer
    import numpy as np

    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.metrics import confusion_matrix,classification_report
    from sklearn.linear_model import LogisticRegression
    
    df = pd.read_csv('Reviews.csv')
    df['sentiment'] = df['Score'].apply(lambda rating : +1 if rating > 3 else -1 if rating < 3 else 0)
    df['sentimentt'] = df['sentiment'].replace({-1 : 'negative'})
    df['sentimentt'] = df['sentimentt'].replace({1 : 'positive'})
    df['sentimentt'] = df['sentimentt'].replace({0 : 'neutral'})
    
    df['Text'] = df['Text'].apply(remove_punctuation)
    df = df.dropna(subset=['Summary'])
    df['Summary'] = df['Summary'].apply(remove_punctuation)
    
    index = df.index
    df['random_number'] = np.random.randn(len(index))
    train = df[df['random_number'] <= 0.8]
    test = df[df['random_number'] > 0.8]
    
    vectorizer = CountVectorizer(token_pattern=r'\b\w+\b')
    train_matrix = vectorizer.fit_transform(train['Summary'])
    test_matrix = vectorizer.transform(test['Summary'])
    
    lr = LogisticRegression(solver='liblinear', max_iter=400)   
    
    X_train = train_matrix
    X_test = test_matrix
    y_train = train['sentiment']
    y_test = test['sentiment']
    
    lr.fit(X_train,y_train)
    
    sentence = []
    sentence.append(sys.argv[1])
    
    sentiment_analysis(sentence)


# In[ ]:





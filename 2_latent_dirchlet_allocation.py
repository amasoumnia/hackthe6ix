# -*- coding: utf-8 -*-
"""
@author: Ali Masoumni
"""
import os
import text_preparation as tp
from gensim import corpora
from gensim.models.ldamodel import LdaModel as lda
import pickle

#set path to training articles
corpus_path = 'corpus/'
article_paths = [os.path.join(corpus_path,p) for p in os.listdir(corpus_path)]

# contents of all of the articles

corpus =[]
#opening and cleaning all of the training articles
for path in article_paths:
    with open(path) as f:
        doc = ''
        try:
            for line in f:
                doc = doc + ' ' + line  
            #Clean the text and extract the token words
            tokens = tp.prepare_text_for_lda(doc)
            if len(tokens) > 0:
                corpus.append(tokens)
        except:
            next

#setting hyperparameters
TOPICS = 3
PASSES = 15
ITERATIONS = 1000

# Creating term dictionary of corpus. Each unique term is assigned an index
dictionary = corpora.Dictionary(corpus)

# Filter terms which appear in fewer than 4 and more than 40%
dictionary.filter_extremes(no_below=4, no_above=0.4)
dictionary.save('LDA Files/dictionary.gensim')

# Converting corpus into document term matrix based on the dictionary above
vectorized_corpus = [dictionary.doc2bow(doc) for doc in corpus]

# save corpus in a pickle file
pickle.dump(vectorized_corpus,open('LDA Files/old_corpus.pickle','wb'))

# creating an object for our model
ldamodel = lda(vectorized_corpus, num_topics=TOPICS, id2word = dictionary, passes = PASSES, iterations = ITERATIONS)
ldamodel.save('LDA Files/model.gensim')

# printing the 5 found topics and the five most associated words with that topic
for i,topic in enumerate(ldamodel.print_topics(num_topics = TOPICS, num_words = 5)):
    words = topic[1].split('+')
    print(words,'\n')


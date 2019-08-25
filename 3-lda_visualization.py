# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 14:40:24 2019

@author: Caelum Kamps
"""

import gensim
import pickle
import pyLDAvis.gensim

# reload dictionary, corpus, and lda model
dictionary = gensim.corpora.Dictionary.load('LDA Files/dictionary.gensim')
corpus = pickle.load(open('LDA Files/old_corpus.pickle','rb'))
lda = gensim.models.ldamodel.LdaModel.load('LDA Files/model.gensim')

# Prepare data for display and save as an html file
lda_display = pyLDAvis.gensim.prepare(lda,corpus,dictionary,sort_topics = False)
pyLDAvis.save_html(lda_display, 'Visualization/lda_vis.html')
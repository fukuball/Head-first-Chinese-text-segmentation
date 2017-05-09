# encoding=utf8
import sys
import os
from gensim import corpora, models, similarities
from six import iteritems
import uniout

dictionary = corpora.Dictionary.load('model/lyrics.dict')
corpus = corpora.MmCorpus('model/lyrics.mm')

lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=28)
index = similarities.MatrixSimilarity(lsi[corpus], num_features=100)
index.save('model/lyrics.index')

lyrics_topic = [];
fp = open("data/lyrics_topic.dataset")
for i, line in enumerate(fp):
    lyrics_topic.append(line)
fp.close()

avg_sim_percent = 0
fp = open("data/lyrics_word_net.dataset")
for i, doc in enumerate(fp):
    this_topic = lyrics_topic[i-1]
    #print("This Topic: "+this_topic)
    vec_bow = dictionary.doc2bow(doc.lower().split())
    vec_lsi = lsi[vec_bow]
    sims = index[vec_lsi]
    sims = sorted(enumerate(sims), key=lambda item: -item[1])
    #print(sims[:5])
    sim_count = 0
    for sim in sims[:5]:
        sim_topic = lyrics_topic[sim[0]]
        #print("Sim Topic: "+sim_topic)
        if sim_topic == this_topic:
            sim_count = sim_count+1
    sim_percent = (sim_count/5.0) * 100
    print(sim_percent)
    if sim_percent == 100:
        print("This Topic: "+this_topic)
        print(sims[:5])
    avg_sim_percent = avg_sim_percent+sim_percent
avg_sim_percent = (avg_sim_percent/240)
print(avg_sim_percent)
fp.close()
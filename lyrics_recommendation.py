# encoding=utf8
import sys
import os
from gensim import corpora, models, similarities
from six import iteritems
import uniout

dictionary = corpora.Dictionary.load('model/lyrics.dict')
corpus = corpora.MmCorpus('model/lyrics.mm')

lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=28)

doc = sys.argv[1]
vec_bow = dictionary.doc2bow(doc.lower().split())
vec_lsi = lsi[vec_bow]

index = similarities.MatrixSimilarity(lsi[corpus], num_features=100)
index.save('model/lyrics.index')

sims = index[vec_lsi]

sims = sorted(enumerate(sims), key=lambda item: -item[1])
print(sims[:5])

lyrics = [];
fp = open("data/lyrics_word_net.dataset")
for i, line in enumerate(fp):
    lyrics.append(line)
fp.close()

for lyric in sims[:5]:
    print "\n相似歌詞：",  lyrics[lyric[0]]
    print "相似度：",  lyric[1]
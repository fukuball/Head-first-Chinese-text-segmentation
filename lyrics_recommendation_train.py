# encoding=utf8

import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

import os
from gensim import corpora, models, similarities
from six import iteritems
import uniout

input_train_data_file = os.path.join(os.path.join(os.getcwd(), os.path.dirname(__file__)), 'data/lyrics_word_net.dataset')
stop_word_file = os.path.join(os.path.join(os.getcwd(), os.path.dirname(__file__)), 'data/stop_words.txt')

with open(stop_word_file) as f:
    stop_word_content = f.readlines()
stop_word_content = [x.strip() for x in stop_word_content]
stop_word_content = " ".join(stop_word_content)

dictionary = corpora.Dictionary(document.split() for document in open(input_train_data_file))
stoplist = set(stop_word_content.split())
stop_ids = [dictionary.token2id[stopword] for stopword in stoplist
            if stopword in dictionary.token2id]
dictionary.filter_tokens(stop_ids)
dictionary.compactify()
dictionary.save('model/lyrics.dict')

texts = [[word for word in document.split() if word not in stoplist]
         for document in open(input_train_data_file)]

# remove words that appear only once
from collections import defaultdict
frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1

texts = [[token for token in text if frequency[token] >= 1]
         for text in texts]

corpus = [dictionary.doc2bow(text) for text in texts]
corpora.MmCorpus.serialize('model/lyrics.mm', corpus)

##################

if (os.path.exists("model/lyrics.dict")):
    dictionary = corpora.Dictionary.load('model/lyrics.dict')
    corpus = corpora.MmCorpus('model/lyrics.mm')
    print("Used files generated from first tutorial")
else:
    print("Please run first tutorial to generate data set")

tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]

lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=28)
corpus_lsi = lsi[corpus_tfidf]

lsi.save('model/lyrics.lsi')
lsi = models.LsiModel.load('model/lyrics.lsi')

##################

dictionary = corpora.Dictionary.load('model/lyrics.dict')
corpus = corpora.MmCorpus('model/lyrics.mm')

lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=28)
print('debug 0')
print(lsi.show_topic(0, topn=20))
print('debug 1')
print(lsi.show_topic(1, topn=20))
print('debug 2')
print(lsi.show_topic(2, topn=20))
print('debug 3')
print(lsi.show_topic(3, topn=20))
print('debug 4')
print(lsi.show_topic(4, topn=20))
print('debug 5')
print(lsi.show_topic(5, topn=20))
print('debug 6')
print(lsi.show_topic(6, topn=20))
print('debug 7')
print(lsi.show_topic(7, topn=20))
print('debug 8')
print(lsi.show_topic(8, topn=20))
print('debug 9')
print(lsi.show_topic(9, topn=20))
print('debug 10')
print(lsi.show_topic(10, topn=20))
print('debug 11')
print(lsi.show_topic(11, topn=20))
print('debug 12')
print(lsi.show_topic(12, topn=20))
print('debug 13')
print(lsi.show_topic(13, topn=20))
print('debug 14')
print(lsi.show_topic(14, topn=20))
print('debug 15')
print(lsi.show_topic(15, topn=20))
print('debug 16')
print(lsi.show_topic(16, topn=20))
print('debug 17')
print(lsi.show_topic(17, topn=20))
print('debug 18')
print(lsi.show_topic(18, topn=20))
print('debug 19')
print(lsi.show_topic(19, topn=20))
print('debug 20')
print(lsi.show_topic(20, topn=20))
print('debug 21')
print(lsi.show_topic(21, topn=20))
print('debug 22')
print(lsi.show_topic(22, topn=20))
print('debug 23')
print(lsi.show_topic(23, topn=20))
print('debug 24')
print(lsi.show_topic(24, topn=20))
print('debug 25')
print(lsi.show_topic(25, topn=20))
print('debug 26')
print(lsi.show_topic(26, topn=20))
print('debug 27')
print(lsi.show_topic(27, topn=20))
print('debug')

doc = "沒有 山 不能 跨越 沒有 海 不能 冒險 讓 歷史 記得 這 一天 當我 用心 立下 諾言 沒有 事 不能 改變 沒有 夢 不能 實現 我 站 在 未來 最 前線 抬頭 迎接 每個 考驗 海闊天空 是 我 的 地圖 想 寫下 全新 紀錄 放眼 天下 在 等 我 去 征服 用 熱血 燃燒 黑夜 等待 最 燦爛 的 日出 看 陽光 與 我 賽跑 風雨 和 我 狂飆 我 的 驕傲 自己 打造 每個 夢 永遠 比天 高 一顆 心 為 希望 在 跳躍 讓 世界 為 我 歡呼 大地 為 我 炫耀 我 的 驕傲 你 會 看到 汗 和 淚 痛苦 的 煎熬 在 這 一刻 都 是 我 光榮 的 記號 海闊天空 是 我 的 地圖 想 寫下 全新 紀錄 放眼 天下 在 等 我 去 征服 用 熱血 燃燒 黑夜 等待 最 燦爛 的 日出 看 陽光 與 我 賽跑 風雨 和 我 狂飆 我 的 驕傲 自己 打造 每個 夢 永遠 比天 高 一顆 心 為 希望 在 跳躍 讓 世界 為 我 歡呼 大地 為 我 炫耀 我 的 驕傲 你 會 看到 汗 和 淚 ~ 痛苦 的 煎熬 在 這 一刻 都 是 我 ~ 光榮 的 記號 看 陽光 與 我 賽跑 風雨 和 我 狂飆 我 的 驕傲 自己 打造 每個 夢 ~ 永遠 比天 高 一顆 心 ~ 為 希望 在 跳躍 在 跳躍 ) 讓 世界 為 我 歡呼 大地 為 我 炫耀 我 的 驕傲 你 會 看到 你 會 看到 汗 和 淚 痛苦 的 煎熬 在 這 一刻 都 是 我 光榮 的 記號"
vec_bow = dictionary.doc2bow(doc.lower().split())
vec_lsi = lsi[vec_bow]

index = similarities.MatrixSimilarity(lsi[corpus], num_features=100)
index.save('model/lyrics.index')

sims = index[vec_lsi]

sims = sorted(enumerate(sims), key=lambda item: -item[1])
print(sims[:5])

'''
lyrics = [];
fp = open("data/lyrics_word_net.dataset")
for i, line in enumerate(fp):
    lyrics.append(line)
fp.close()

for lyric in sims[:5]:
    print "\n相似歌詞：",  lyrics[lyric[0]]
    print "相似度：",  lyric[1]
'''
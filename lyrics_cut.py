#encoding=utf-8
import jieba
import codecs

jieba.set_dictionary("data/dict.txt.big")

wf = codecs.open('data/lyrics_cut.dataset', "w", "utf-8")

with open('data/lyrics.dataset', 'rb') as f:
    for line in f:
        words = jieba.cut(line)
        wf.write(u" ".join(words))
        print(line)

wf.close()
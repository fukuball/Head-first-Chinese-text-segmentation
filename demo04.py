#encoding=utf-8
import jieba
import jieba.posseg as pseg

jieba.set_dictionary("data/dict.txt.big")

words = pseg.cut("颱風就是要泛舟啊不然要幹嘛")
for word, flag in words:
    print('%s %s' % (word, flag))
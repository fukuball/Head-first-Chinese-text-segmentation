#encoding=utf-8
import jieba

jieba.set_dictionary("data/dict.txt.big")

result = jieba.tokenize(u'圖畫裡，龍不吟，虎不嘯，小小書僮可笑可笑')
for tk in result:
    print("word %s\t\t start: %d \t\t end:%d" % (tk[0],tk[1],tk[2]))
#encoding=utf-8
import jieba

jieba.set_dictionary("data/dict.txt.big")

content = open('data/lyric1.txt', 'rb').read()

print "Input：", content

words = jieba.cut(content)
print(" / ".join(words))
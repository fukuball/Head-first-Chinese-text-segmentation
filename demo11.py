#encoding=utf-8
import jieba

jieba.set_dictionary("data/dict.txt.big")
jieba.load_userdict("data/userdict.txt")

content = open('data/lyric2.txt', 'rb').read()

print "Input：", content

words = jieba.cut(content)
print(" / ".join(words))
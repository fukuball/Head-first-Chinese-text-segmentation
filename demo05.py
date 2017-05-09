#encoding=utf-8
import jieba

content = open('data/lyric1.txt', 'rb').read()

print "Input：", content

words = jieba.cut(content)
print(" / ".join(words))
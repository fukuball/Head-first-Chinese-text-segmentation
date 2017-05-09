#encoding=utf-8
import jieba
import jieba.analyse

jieba.set_dictionary("data/dict.txt.big")
jieba.analyse.set_stop_words("data/stop_words.txt")

content = open('data/lyric1.txt', 'rb').read()

print "Input：", content

tags = jieba.analyse.extract_tags(content, 10)
print "Output："
print(" / ".join(tags))
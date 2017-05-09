# encoding=utf-8
import jieba

jieba.set_dictionary('data/dict.txt.big')

seg_list = jieba.cut("全台大停電")
print(" / ".join(seg_list))

jieba.add_word("全台", freq=100)
seg_list = jieba.cut("全台大停電")
print(" / ".join(seg_list))
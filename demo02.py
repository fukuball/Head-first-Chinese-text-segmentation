#encoding=utf-8
import jieba

jieba.set_dictionary("data/dict.txt.big")

seg_list = jieba.cut("我來到北京清華大學")
print(" / ".join(seg_list))

seg_list = jieba.cut("我來到北京清華大學", cut_all=True)
print(" / ".join(seg_list))
# encoding=utf-8
import jieba

jieba.set_dictionary('data/dict.txt.big')

seg_list = jieba.cut("下雨天留客天留我不留")
print(" / ".join(seg_list))

seg_list = jieba.cut("海水朝朝朝朝朝朝朝落；浮雲長長長長長長長消。")
print(" / ".join(seg_list))

seg_list = jieba.cut("海水潮，朝朝潮，朝潮朝落；浮雲長，常常長，常長常消。")
print(" / ".join(seg_list))
# encoding=utf-8
import jieba

jieba.set_dictionary('data/dict.txt.big')

seg_list = jieba.cut("塵世中一個迷途小書僮")
print(" / ".join(seg_list))

seg_list = jieba.cut("我們在野生動物園玩")
print(" / ".join(seg_list)) # 歧異詞辨識

seg_list = jieba.cut("林志傑是結巴PHP的作者")
print(" / ".join(seg_list)) # 新詞辨識
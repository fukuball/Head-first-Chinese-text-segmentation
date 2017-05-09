#encoding=utf-8
import jieba
import codecs

word_net = []

with open('data/word_net.txt', 'rb') as f:
    for line in f:
        word_net.append(line)

word_net = sorted(set(word_net))
word_net_dic = {}

for word in word_net:
    word_s = word.split()
    word_net_dic[word_s[0]] = word_s[1]

wf = open('data/lyrics_word_net.dataset', "wb")

with open('data/lyrics_cut.dataset', 'rb') as f:
    for line in f:
        line_words = line.split()
        line_lyrics = ''
        for line_word in line_words:
            if line_word in word_net_dic:
                line_lyrics = line_lyrics + word_net_dic[line_word] + ' '
            else:
                line_lyrics = line_lyrics + line_word + ' '
        print(line_lyrics+"\n")
        wf.write(line_lyrics+"\n")

wf.close()
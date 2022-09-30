
import jieba
import math
import time
import re

class TraversalFun():

    # 1 初始化
    def __init__(self, rootDir):
        self.rootDir = rootDir

    def TraversalDir(self):
        return TraversalFun.getCorpus(self, self.rootDir)

    def getCorpus(self, rootDir):
        corpus = []
        r1 = u'[a-zA-Z0-9’!"#$%&\'()*+,-./:：;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~]+'  # 用户也可以在此进行自定义过滤字符
        count=0
        with open(rootDir, "r", encoding='utf-8') as file:
            filecontext = file.read();
            filecontext = re.sub(r1, '', filecontext)
            filecontext = filecontext.replace("\n", '')
            filecontext = filecontext.replace(" ", '')

            #seg_list = jieba.cut(filecontext, cut_all=True)
            #corpus += seg_list
            count += len(filecontext)
            corpus.append(filecontext)
        return corpus,count

def cal_unigram(corpus,count):
    before = time.time()
    split_words = []
    words_len = 0
    line_count = 0
    words_tf={}
    for line in corpus:
        for x in jieba.cut(line):
            split_words.append(x)
            words_len += 1
        get_tf(words_tf, split_words)
        split_words = []
        line_count += 1
    count_0=[]
    words_len_0=[]
    entropy_0=[]
    count_0.append(count)
    words_len_0.append(words_len)

    print("语料库字数:", count)
    print("分词个数:", words_len)
    print("平均词长:", round(count / words_len, 5))
    entropy = []
    for uni_word in words_tf.items():
        entropy.append(-(uni_word[1] / words_len) * math.log(uni_word[1] / words_len, 2))
    en=round(sum(entropy), 5)
    entropy_0.append(en)
    print("基于词的一元模型的中文信息熵为:",en , "比特/词")
    after = time.time()
    print("运行时间:", round(after - before, 5), "s")
    return entropy_0

# 词频统计，方便计算信息熵
def get_tf(tf_dic, words):

    for i in range(len(words)-1):
        tf_dic[words[i]] = tf_dic.get(words[i], 0) + 1



if __name__ == '__main__':

    #tra ='' #TraversalFun("/Users/renee/Downloads/datachinanewswenhua.txt")

    for i in range(1,50):
        print(i)
        path='/Users/renee/Documents/'+str(i)+'.txt'
        with open(path) as data:
            datacontext=data.read()
        data.close()
        with open("/Users/renee/Downloads/d1.txt",'a') as data_1:
            data_1.write(datacontext)

        add_tra = TraversalFun("/Users/renee/Downloads/d1.txt" ) # 需要进行分割的文件，请修改文件名
        corpus,count=add_tra.TraversalDir()
        cal_unigram(corpus, count)
entropy_0=[12.33908,12.33847,12.33794,12.33778,12.33648,12.33472,12.33318,12.33084,12.32897,12.32728,12.32443,12.32196,12.31967,12.317,
           12.31446,12.3115,12.30876,12.30575,12.30298,12.29999,12.29742,12.29498,12.29247,12.29077,12.28856,12.28641,12.28423,
           12.28208,12.28007,12.27769,12.2755,12.27347,12.27111,12.27382,12.2768,12.27906,12.28134,12.28365,12.28589,12.28793,12.29039,
           12.29229,12.29399,12.29542,12.29698,12.29931,12.30167,12.30372,12.30605]
import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(20,102,40)
plt.title('Change of Shannon Entropy for Chinese texts')
plt.xlabel('File Size(M)')
plt.ylabel('Shannon Entropy(Bits/letter）')
plt.plot(x, entropy_0[9::],color='purple'
         )

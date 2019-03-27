#coding=gbk
#python 生成词云


#简单词云
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba

#加载文件内容
text_from_file_with_apath = open('D:/thisme_D/Python/python_study/demo/hello.txt',encoding='utf-8').read()

#结巴分词器分词
wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all=True)
wl_space_split = " ".join(wordlist_after_jieba)

#云图的生成
my_wordcloud = WordCloud(background_color="white",width=1000,height=860, font_path="C:\\Windows\\Fonts\\STFANGSO.ttf").generate(wl_space_split)

#显示
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()

#词云Demo

import jieba.analyse
from PIL import Image,ImageSequence
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator

article= open('D:/thisme_D/Python/python_study/demo/hello.txt',encoding='utf-8').read()

result=jieba.analyse.textrank(article,topK=50,withWeight=True)
keywords = dict()
for i in result:
    keywords[i[0]]=i[1]
print(keywords)

#获取原型图片
image= Image.open('D:/thisme_D/Python/python_study/demo/timg.jpg')
graph = np.array(image)
wc = WordCloud(font_path='C:/Windows/fonts/simhei.ttf',background_color='white',max_words=50,mask=graph,width=700,height=1244)
wc.generate_from_frequencies(keywords)
image_color = ImageColorGenerator(graph)
plt.imshow(wc)
plt.imshow(wc.recolor(color_func=image_color))
plt.axis("off")
plt.show()
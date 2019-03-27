#coding=gbk
#python ���ɴ���


#�򵥴���
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba

#�����ļ�����
text_from_file_with_apath = open('D:/thisme_D/Python/python_study/demo/hello.txt',encoding='utf-8').read()

#��ͷִ����ִ�
wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all=True)
wl_space_split = " ".join(wordlist_after_jieba)

#��ͼ������
my_wordcloud = WordCloud(background_color="white",width=1000,height=860, font_path="C:\\Windows\\Fonts\\STFANGSO.ttf").generate(wl_space_split)

#��ʾ
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()

#����Demo

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

#��ȡԭ��ͼƬ
image= Image.open('D:/thisme_D/Python/python_study/demo/timg.jpg')
graph = np.array(image)
wc = WordCloud(font_path='C:/Windows/fonts/simhei.ttf',background_color='white',max_words=50,mask=graph,width=700,height=1244)
wc.generate_from_frequencies(keywords)
image_color = ImageColorGenerator(graph)
plt.imshow(wc)
plt.imshow(wc.recolor(color_func=image_color))
plt.axis("off")
plt.show()
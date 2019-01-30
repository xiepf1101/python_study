#coding=utf-8
#image
import sys
print(sys.path)
sys.path[0] = 'D:\thisme_D\Python\Anaconda3\Lib\site-packages'
from fastai import *
from fastai.vision import *
import matplotlib.pyplot as plt

from PIL import Image

a = 1
b = a + 1
c = b + a + 1
d = c + b + a +1
print(str(a)+", "+str(b)+", "+str(c)+", "+str(d))

#plt.plot([a,b,c,d])
#plt.show()

help(untar_data)

filepath = "D:/thisme_D/Python/python_study/workspaceDemo/oxford-iiit-pet"
print(URLs.PETS)
path = untar_data(URLs.PETS); path

path.ls()

path_anno = path/'annotations'
path_img = path/'images'

fnames = get_image_files(path_img)

fnames[:5]

pp.random.seed(2)
pat = r'/([^/]+)_\d+.jpg$'

data = ImageDataBunch.from_name_re(path_img, fnames, pat, ds_tfms=get_transfroms(), size=224)
data.normalize(imagenet_stats)

data.show_batch(rows=3, figsize=(7,6))

print(data.classes)
len(data,classes),data.c

learn = ConvLearner(data, models.resnet34, metrics=error_rate)

learn.fit_one_cycle(4)

learn.save('stage-1')

interp = ClassificationInterpretation.from_learner(learn)

interp.plot_top_losses(9, figsize=(15,11))

doc(interp.plot_top_losses)

interp.plot_confusion_matrix(figsize=(12,12), dpi=60)

interp.most_confused(min_val=2)

learn.unfreeze()

learn.fit_one_cycle(1)

learn.load('stage-1')

learn.lr_find()

learn.recorder.plot()

learn.unfreeze()

learn.fit_one_cycle(2, max_lr=slice(1e-6,1e-4))

data = ImageDataBunch.from_name_re(path_img, fnames, pat, ds_tfms=get_transfroms())
data.normalize(imagenet_stats)

learn = ConvLearner(data, models.resnet50, metrics=error_rate)

learn.fit_one_cycle(5)

learn.save('stage-1-50')

learn.unfreeze()

learn.fit_one_cycle(1, max_lr=silce(1e-6,1e-4))

learn.load('stage-1-50')

interp = ClassificationInterpretation.from_learner(learn)

interp.most_confused(min_val=2)

path = untar_data(URLs.MNIST_SAMPLE); path

tfms = get_transfroms(do_flip=False)
data = ImageDataBunch.from_folder(path, ds_tfms=tfms, size = 26)

data.show_batch(rows=3, figsize=(5,5))

learn = ConvLearner(data, models.resnet18, metrics=accuracy)
learn.fit(2)

df = pd.read_csv(path/'labels.csv')
df.head()

data = ImageDataBunch.from_csv(path, ds_tfms, size=28)

data.show_batch(rows=3, figsize=(5,5))
data.classes

data = ImageDataBunch.from_df(path, df, ds_tfms=tfms, size=24)
data.classes

fn_paths = [path/name for name in df['name']]; fn_paths[:2]

pat = r"/(\d)/\d+\.png$"
data = ImageDataBunch.from_name_re(path, fn_paths, pat=pat, ds_tfms=tfms, size=24)
data.classes

data = ImageDataBunch.from_name_func(path, fn_paths, ds_tfms=tfms, size=24,
                                     label_func = lambda x: '3' if '/3/' in str(x) else '7')
data.classes

labels = [('3' if '/3/' in str(x) else '7') for x in fn_paths]
labels[:5]

data = ImageDataBunch.from_lists(path, fn_paths, labels=labels, ds_tfms=tfms, size=24)
data.classes
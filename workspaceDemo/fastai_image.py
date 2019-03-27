#coding=utf-8
#imageclassification

from fastai import *
from fastai.vision import *

folder = 'black'
file = 'urls_black.txt'

folder = 'teddys'
file = 'urls_teddys.txt'

folder = 'grizzly'
file = 'urls_grizzly.txt'

#download_images

path = Path('data/bears')
dest = path/folder
dest.mkdir(parents=True, exist_ok=True)

classes = ['teddys','grizzly','black']
download_images(path/file, dest, max_pics=200)

for c in classes:
    print(c)
    verify_images(path/c, delete=True, max_workers=8)

np.random.seed(42)
data = ImageDataBunch.from_folder(path, train=".", valid_pct=0.2,
                                  ds_tfms=get_transforms(), size=224, num_workers=4).normalize(imagenet_stats)
data.classes
data.show_batch(rows=3, figsize=(7,8))

data.classes, data.c, len(data.train_ds), len(data.valid_ds)

#Train Model

learn = create_cnn(data, models.resnet34, metrics=error_rate)
learn.fit_one_cycle(4)
learn.save('stage-1')
learn.unfreeze()
learn.lr_find()
learn.recorder.plot()
learn.fit_one_cycle(2, max_lr=slice(3e-5,3e-4))
learn.save('stage-2')

#interpretation
iterp.load('stage-2')
interp = ClassificationInterpretation.from_learner(learn)
interp.plot_confusion_matrix()

#cleaning up  干扰的数据或者无用的数据清理
from fastai.widgets import *

losses,idxs = interp.top_losses()
top_loss_paths = data.valid_ds.x[idxs]

fd = FileDeleter(file_paths=top_loss_paths)

#Putting your model in production   生产测试
data.classes

#如果不是使用GPU，则进行下面配置。反之则免之
fastai.defaults.device = torch.device('cpu')
img = open_image(path/'black'/'0000021.jpg')
img

classes = ['black', 'grizzly', 'teddys']
data2 = ImageDataBunch.single_from_classes(path, classes, tfms=get_transforms(), size=224).normalize(imagenet_stats)
learn = create_cnn(data2, models.resnet34)
learn.load('stage-2')

pred_class,pred_idx,outputs = learn.predict(img)
pred_class

learn = create_cnn(data, models.resnet34, metrics=error_rate)
learn.fit_one_cycle(1, max_lr=0.5)

learn = create_cnn(data, models.resnet34, metrics=error_rate0)
learn.fit_one_cycle(5, max_lr=1e-5)
learn.recorder.plot_losses()

learn = create_cnn(data, models.resnet34, metrics=error_rate)
learn.fit_one_cycle(1)


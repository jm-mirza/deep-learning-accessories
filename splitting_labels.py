import random
import glob
import os
import pandas as pd

labels = glob.glob(
    os.path.join('/mnt/data2/fog_dataset_with_labels/images/', '*.' + 'png'))

'''
###Uncomment this if you only need a text file with base names###
for index, label in enumerate(labels):
    labels[index] = (label.split('/')[-1]).split('.')[0]
'''

print(len(labels))



random.shuffle(labels)

train_len = int(len(labels) * 0.85)

train_labels = labels[:train_len]
val_labels = labels[train_len:]

for i in range(len(train_labels)):
    for j in range(len(val_labels)):

        if train_labels[i] == val_labels[j]:
            print('Over-writing... Check Again')

print(len(train_labels), ' ', len(val_labels), 'sum = {}'.format(len(train_labels) + len(val_labels)))

frame_train = pd.DataFrame(train_labels)
frame_train.to_csv('train.txt',  index=None)

print('Successfully written to train.txt.')

frame_train_1 = pd.DataFrame(val_labels)
frame_train_1.to_csv('val.txt',  index=None)

print('Successfully written to val.txt.')


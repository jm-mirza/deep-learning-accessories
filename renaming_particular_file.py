import os
import glob
import shutil

image_labels = glob.glob(
    os.path.join('image_2/', '*.' + 'png'))

annotations_labels = glob.glob(
    os.path.join('label_2/', '*.' + 'txt'))

#print(len(annotations_labels))

#print(annotations_labels)
image_dir = 'image_2/'
label_dir = 'label_2/'
i = 0

'''for aindex, alabel in enumerate(image_labels):
    base_name_images = (alabel.split('/')[-1]).split('.')[0]
    #print(base_name_images)

for bindex, blabel in enumerate(annotations_labels):    
    base_name_labels = (blabel.split('/')[-1]).split('.')[0]
'''
#print(len(base_name_images))


for aindex, alabel in enumerate(image_labels):
    base_name_images = (alabel.split('/')[-1]).split('.')[0]    
    base_name_labels = base_name_images        
         #print(base_name_images)


         my_dest_labels ="" + str(i) + ".txt"
         my_dest_images ="" + str(i) + ".png"

         my_source_labels =label_dir + base_name_labels + '.txt'
         my_source_images =image_dir + base_name_images + '.png'

         my_dest_images =image_dir + my_dest_images
         my_dest_labels =label_dir + my_dest_labels

         os.rename(my_source_labels, my_dest_labels)
         os.rename(my_source_images, my_dest_images)
            
    i += 1        
    	     

#print(aindex)
#print(bindex)



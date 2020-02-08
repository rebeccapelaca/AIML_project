import random
import os
from PIL import Image
import numpy as np
import copy as cp


def permutation(same=False):
    # same = False -> the permutation must be diferent from the original
    i=0
    j=1
    k=2
    
    if not same:
        while i==0 and j==1 and k==2:
            i=random.choice([0,1,2])
            j=random.choice([0,1,2])
            while j==i:
                j=random.choice([0,1,2])
            k=random.choice([0,1,2])
            while k==i or k==j:
                k=random.choice([0,1,2])
    else:
        i=random.choice([0,1,2])
        j=random.choice([0,1,2])
        while j==i:
            j=random.choice([0,1,2])
        k=random.choice([0,1,2])
        while k==i or k==j:
            k=random.choice([0,1,2])
    
    return i,j,k
    
def change_color(img):
    pixels = img.load()
    width, height = img.size
    
    first = True
    ch=np.zeros(3)
    i=j=k=0
    for y in range(height):
        for x in range(width):
            r,g,b=pixels[x,y]
            if first:
                i,j,k=permutation(same=False)     # compute permutation of rgb
                first=False                     # The permutation will be the same for 
                                                # the whole image. The image will
                                                # always be changed due to same=False
            ch[i]=r
            ch[j]=g
            ch[k]=b
            
            pixels[x,y]=(int(ch[0]),int(ch[1]),int(ch[2]))
    return img
   
dataset = '/home/rebecca/Desktop/AIML_working_area/dataset'
clipart = '/home/rebecca/Desktop/AIML_working_area/clipart'

path_1 = clipart + '/pencil'
path_2 = clipart + '/postcard'
path_3 = clipart + '/shorts'
path_4 = clipart + '/hat'
path_5 = clipart + '/jacket'
path_6 = clipart + '/guitar'
path_7 = clipart + '/saxophone'
path_8 = clipart + '/piano'
path_9 = clipart + '/clarinet'
path_10 = clipart + '/smiley_face'
path_11 = clipart + '/angel'
path_12 = clipart + '/mermaid'
path_13 = clipart + '/bracelet'
path_14 = clipart + '/belt'
path_15 = clipart + '/table'
path_16 = clipart + '/chair'
path_17 = clipart + '/drill'
path_18 = clipart + '/bowtie'
path_19 = clipart + '/helmet'
path_20 = clipart + '/mountain'

paths = [path_1, path_2, path_3, path_4, path_5, path_6, path_7, path_8, path_9,
         path_10, path_11, path_12, path_13, path_14, path_15, path_16, path_17,
         path_18, path_19, path_20]

""" 
path_1 = clipart + '/grapes'
path_2 = clipart + '/apple'
path_3 = clipart + '/pear'
path_4 = clipart + '/watermelon'
path_5 = clipart + '/carrot'
path_6 = clipart + '/cookie'
path_7 = clipart + '/ice_cream'
path_8 = clipart + '/kangaroo'
path_9 = clipart + '/pig'
path_10 = clipart + '/rabbit'
path_11 = clipart + '/raccoon'
path_12 = clipart + '/tree'
path_13 = clipart + '/octagon'
path_14 = clipart + '/basketball'
path_15 = clipart + '/book'
path_16 = clipart + '/umbrella'
path_17 = clipart + '/teddy-bear'
path_18 = clipart + '/tent'
path_19 = clipart + '/marker'
path_20 = clipart + '/t-shirt'

paths = [path_1, path_2, path_3, path_4, path_5, path_6, path_7, path_8, path_9,
         path_10, path_11, path_12, path_13, path_14, path_15, path_16, path_17,
         path_18, path_19, path_20]


path_1 = clipart + '/bus'
path_2 = clipart + '/helicopter'
path_3 = clipart + '/airplane'
path_4 = clipart + '/car'
path_5 = clipart + '/bird'
path_6 = clipart + '/duck'
path_7 = clipart + '/sea_turtle'
path_8 = clipart + '/shark'
path_9 = clipart + '/sheep'
path_10 = clipart + '/squirrel'
path_11 = clipart + '/bear'
path_12 = clipart + '/fish'
path_13 = clipart + '/frog'
path_14 = clipart + '/lion'
path_15 = clipart + '/swan'
path_16 = clipart + '/tiger'
path_17 = clipart + '/camel'
path_18 = clipart + '/cat'
path_19 = clipart + '/crocodile'
path_20 = clipart + '/octopus'

paths = [path_1, path_2, path_3, path_4, path_5, path_6, path_7, path_8, path_9,
         path_10, path_11, path_12, path_13, path_14, path_15, path_16, path_17,
         path_18, path_19, path_20]

   
cartoon ='C:\\Users\\Marianna\\Desktop\\AIML_project\\AIML_project\\cartoon'

dog_path = cartoon+'\\dog'
elephant_path = cartoon+'\\elephant'
giraffe_path = cartoon+'\\giraffe'
guitar_path = cartoon+'\\guitar'
horse_path = cartoon+'\\horse'
house_path = cartoon+'\\house'
person_path = cartoon+'\\person'

paths = [dog_path, elephant_path, giraffe_path, guitar_path, 
         horse_path, house_path, person_path]
"""

count1 = 1388
count2 = 1388
count3 = 1388
count4 = 1456
       
if not os.path.exists(dataset):
                os.mkdir(dataset)
 
for path1 in paths:
    
    path_len1 = len(os.listdir(path1))
    indx = int(path_len1/4)
    print(path_len1)
    
    count = 0

    for img_file in os.listdir(path1):
        odd = Image.open(path1 + '/' + img_file)
        img_orig = cp.copy(odd)
        odd = change_color(odd)
        #odd.show()
        #img_orig.show()
    
        count = count + 1
    
        if count<=indx:
            # odd = immagine 1
            count1 = count1 + 1
            label1_path = dataset+'/1'
            
            if not os.path.exists(label1_path):
                os.mkdir(label1_path)
                
            label1_path = label1_path+'/'+str(count1) # folder name of this dataset entry
            if not os.path.exists(label1_path):
                os.mkdir(label1_path)
                
            odd.save(label1_path+'/1.jpg')
            img_orig.save(label1_path+'/2.jpg')
            img_orig.save(label1_path+'/3.jpg')
            img_orig.save(label1_path+'/4.jpg')
            # break        
        elif count>indx and count<=indx*2:
            # odd = immagine 2
            count2 = count2 + 1
            label2_path = dataset+'/2'
            
            if not os.path.exists(label2_path):
                os.mkdir(label2_path)
                
            label2_path = label2_path+'/'+str(count2)
            if not os.path.exists(label2_path):
                os.mkdir(label2_path)
                
            img_orig.save(label2_path+'/1.jpg')
            odd.save(label2_path+'/2.jpg')
            img_orig.save(label2_path+'/3.jpg')
            img_orig.save(label2_path+'/4.jpg')

        elif count>indx*2 and count<=indx*3:
            # odd = immagine 3
            count3 = count3 + 1
            label3_path = dataset+'/3'
            
            if not os.path.exists(label3_path):
                os.mkdir(label3_path)
                
            label3_path = label3_path +'/'+str(count3)
            if not os.path.exists(label3_path):
                os.mkdir(label3_path)
                
            img_orig.save(label3_path+'/1.jpg')
            img_orig.save(label3_path+'/2.jpg')
            odd.save(label3_path+'/3.jpg')
            img_orig.save(label3_path+'/4.jpg')

        else:
            # odd = immagine 4
            count4 = count4 + 1
            label4_path = dataset+'/4'
            
            if not os.path.exists(label4_path):
                os.mkdir(label4_path)            
            
            label4_path = label4_path +'/'+str(count4)
            if not os.path.exists(label4_path):
                os.mkdir(label4_path)
                
            img_orig.save(label4_path+'/1.jpg')
            img_orig.save(label4_path+'/2.jpg')
            img_orig.save(label4_path+'/3.jpg')
            odd.save(label4_path+'/4.jpg')
    #break
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 18:42:40 2020

@author: rebecca
"""

import random
import os
from PIL import Image

initial_dataset_cartoon = '/home/rebecca/Desktop/ML_project/datasets/cartoon/initial_dataset'

dog_path_cartoon = initial_dataset_cartoon + '/dog'
elephant_path_cartoon = initial_dataset_cartoon + '/elephant'
giraffe_path_cartoon = initial_dataset_cartoon + '/giraffe'
guitar_path_cartoon = initial_dataset_cartoon + '/guitar'
horse_path_cartoon = initial_dataset_cartoon + '/horse'
house_path_cartoon = initial_dataset_cartoon + '/house'
person_path_cartoon = initial_dataset_cartoon + '/person'

initial_dataset_art_painting = '/home/rebecca/Desktop/ML_project/datasets/art_painting/initial_dataset'

dog_path_art_painting = initial_dataset_art_painting + '/dog'
elephant_path_art_painting = initial_dataset_art_painting + '/elephant'
giraffe_path_art_painting = initial_dataset_art_painting + '/giraffe'
guitar_path_art_painting = initial_dataset_art_painting + '/guitar'
horse_path_art_painting = initial_dataset_art_painting + '/horse'
house_path_art_painting = initial_dataset_art_painting + '/house'
person_path_art_painting = initial_dataset_art_painting + '/person'

initial_dataset_photo = '/home/rebecca/Desktop/ML_project/datasets/photo/initial_dataset'

dog_path_photo = initial_dataset_photo + '/dog'
elephant_path_photo = initial_dataset_photo + '/elephant'
giraffe_path_photo = initial_dataset_photo + '/giraffe'
guitar_path_photo = initial_dataset_photo + '/guitar'
horse_path_photo = initial_dataset_photo + '/horse'
house_path_photo = initial_dataset_photo + '/house'
person_path_photo = initial_dataset_photo + '/person'

initial_dataset_sketch = '/home/rebecca/Desktop/ML_project/datasets/sketch/initial_dataset'

dog_path_sketch = initial_dataset_sketch + '/dog'
elephant_path_sketch = initial_dataset_sketch + '/elephant'
giraffe_path_sketch = initial_dataset_sketch + '/giraffe'
guitar_path_sketch = initial_dataset_sketch + '/guitar'
horse_path_sketch = initial_dataset_sketch + '/horse'
house_path_sketch = initial_dataset_sketch + '/house'
person_path_sketch = initial_dataset_sketch + '/person'

paths = [dog_path_cartoon, elephant_path_cartoon, giraffe_path_cartoon, 
         guitar_path_cartoon, horse_path_cartoon, house_path_cartoon, person_path_cartoon,
         dog_path_art_painting, elephant_path_art_painting, giraffe_path_art_painting, 
         guitar_path_art_painting, horse_path_art_painting, house_path_art_painting, person_path_art_painting,
         dog_path_photo, elephant_path_photo, giraffe_path_photo, 
         guitar_path_photo, horse_path_photo, house_path_photo, person_path_photo,
         dog_path_sketch, elephant_path_sketch, giraffe_path_sketch, 
         guitar_path_sketch, horse_path_sketch, house_path_sketch, person_path_sketch]

dataset = '/home/rebecca/Desktop/ML_project/datasets/mix'

count1 = 0
count2 = 0
count3 = 0
count4 = 0
        
for path1 in paths:
    
    path_len1 = len(os.listdir(path1))
    indx = int(path_len1/4)
    print(path_len1)
    
    count = 0

    for img_file in os.listdir(path1):
        
        flag = False
        
        im1 = Image.open(path1 + '/' + img_file)
        count = count + 1
        
        domain = path1.split("/")[6]
        category = path1.split("/")[8]
        
        num1 = random.randint(0, 27)
        num2 = random.randint(0, 27)
            
        while flag == False:
            if num1 != num2 and paths[num1].find(domain) == -1 and paths[num2].find(domain) == -1 and paths[num1].find(category) != -1 and paths[num2].find(category) != -1:
                flag = True
            else:
                num1 = random.randint(0, 27)
                num2 = random.randint(0, 27)
        
        
        path2 = paths[num1]
        path3 = paths[num2]
        path_len2 = len(os.listdir(path2))
        path_len3 = len(os.listdir(path3))
        
        num3 = random.randint(1, path_len2)
        num4 = random.randint(1, path_len3)
            
        im2 = Image.open(path2 + '/img_' + str(num3) + '.jpg')
        im3 = Image.open(path3 + '/img_' + str(num4) + '.jpg')
        
        for path4 in paths:
            
            if path4.find(domain) == -1 and path4.find(category) == -1:
                
                path_len2 = len(os.listdir(path4))
                num = random.randint(1, path_len2)
                odd = Image.open(path4 + '/img_' + str(num) + '.jpg')
        
                if count<=indx:
                    # odd = immagine 1
                    count1 = count1 + 1
                    label1_path = dataset+'/1/'+str(count1)
                    
                    if not os.path.exists(label1_path):
                        os.mkdir(label1_path)
                   
                    odd.save(label1_path+'/1.jpg')
                    im1.save(label1_path+'/2.jpg')
                    im2.save(label1_path+'/3.jpg')
                    im3.save(label1_path+'/4.jpg')
        
                elif count>indx and count<=indx*2:
                    # odd = immagine 2
                    count2 = count2 + 1
                    label2_path = dataset+'/2/'+str(count2)
                    
                    if not os.path.exists(label2_path):
                        os.mkdir(label2_path)
                        
                    im1.save(label2_path+'/1.jpg')
                    odd.save(label2_path+'/2.jpg')
                    im2.save(label2_path+'/3.jpg')
                    im3.save(label2_path+'/4.jpg')
        
                elif count>indx*2 and count<=indx*3:
                    # odd = immagine 3
                    count3 = count3 + 1
                    label3_path = dataset+'/3/'+str(count3)
                    
                    if not os.path.exists(label3_path):
                        os.mkdir(label3_path)
                        
                    im1.save(label3_path+'/1.jpg')
                    im2.save(label3_path+'/2.jpg')
                    odd.save(label3_path+'/3.jpg')
                    im3.save(label3_path+'/4.jpg')
        
                else:
                    # odd = immagine 4
                    count4 = count4 + 1
                    label4_path = dataset+'/4/'+str(count4)
                    
                    if not os.path.exists(label4_path):
                        os.mkdir(label4_path)            
                    
                    im1.save(label4_path+'/1.jpg')
                    im2.save(label4_path+'/2.jpg')
                    im3.save(label4_path+'/3.jpg')
                    odd.save(label4_path+'/4.jpg')
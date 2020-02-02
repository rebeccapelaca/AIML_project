#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 17:17:55 2020

@author: rebecca
"""
import random
import os
from PIL import Image

#initial_dataset = '/home/rebecca/Desktop/ML_project/datasets/art_painting/initial_dataset'
initial_dataset = '/home/rebecca/Desktop/AIML_project/datasets/cartoon/initial_dataset'
#initial_dataset = '/home/rebecca/Desktop/ML_project/datasets/photo/initial_dataset'
#initial_dataset = '/home/rebecca/Desktop/ML_project/datasets/sketch/initial_dataset'

dog_path = initial_dataset + '/dog'
elephant_path = initial_dataset + '/elephant'
giraffe_path = initial_dataset + '/giraffe'
guitar_path = initial_dataset + '/guitar'
horse_path = initial_dataset + '/horse'
house_path = initial_dataset + '/house'
person_path = initial_dataset + '/person'

paths = [dog_path, elephant_path, giraffe_path, guitar_path, 
         horse_path, house_path, person_path]

#dataset = '/home/rebecca/Desktop/ML_project/datasets/art_painting/dataset2.2'
dataset = '/home/rebecca/Desktop/ML_project/cartoon/dataset2.2'
#dataset = '/home/rebecca/Desktop/ML_project/datasets/photo/dataset2.2'
#dataset = '/home/rebecca/Desktop/ML_project/datasets/sketch/dataset2.2'

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
    
        for path2 in paths:
            
            if path1 != path2:
                
                num1 = random.randint(1, path_len1)
                num2 = random.randint(1, path_len1)
                
                while flag == False:
                    if num1!=num2 and img_file.find(str(num1))==-1 and img_file.find(str(num2))==-1:
                        flag = True
                    else:
                        num1 = random.randint(1, path_len1)
                        num2 = random.randint(1, path_len1)
                        
                im2 = Image.open(path1 + '/img_' + str(num1) + '.jpg')
                im3 = Image.open(path1 + '/img_' + str(num2) + '.jpg')
                
                path_len2 = len(os.listdir(path2))
                num = random.randint(1, path_len2)
                odd = Image.open(path2 + '/img_' + str(num) + '.jpg')
        
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

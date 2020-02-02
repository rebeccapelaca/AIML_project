#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 21:53:14 2020

@author: Nicola
"""


import random
import os
from PIL import Image



dataset = '/home/rebecca/Desktop/ML_project/semantic_dataset'
clipart_path = '/home/rebecca/Desktop/ML_project/clipart'

# set con più elementi dalla stessa cartella
#   csv_quaterne_same_folder.txt

# set solo con elementi di cartelle diverse 
#  csv_quaterne.txt
quad_file = 'C:\\Users\\Marianna\\Desktop\\csv_quaterne_same_folder.txt'

same_folder = False     # da mettere a True se più elementi vengono presi dalla stessa cartella
file =  open(quad_file)

count1 = 0
count2 = 0
count3 = 0
count4 = 0

# creo la cartella per i risultati. Creo anche le quattro sottocartelle
if not os.path.exists(dataset):
    os.mkdir(dataset)
    os.mkdir(dataset+"\\1")
    os.mkdir(dataset+"\\2")
    os.mkdir(dataset+"\\3")
    os.mkdir(dataset+"\\4")
    
for line in file.readlines():
    
    print(line)
    row = line.split(',')
    print(row)
    #print(row[0])
    
    odd_path = clipart_path + '/' + row[0].rstrip('\n')
    first_path = clipart_path + '/' + row[1].rstrip('\n')
    second_path = clipart_path + '/' + row[2].rstrip('\n')
    third_path = clipart_path + '/' + row[3].rstrip('\n')

    num = range(32)    
        
    for n in num:
        
        num1 = random.randint(1, len(os.listdir(first_path)))
        num2 = random.randint(1, len(os.listdir(second_path)))
        num3 = random.randint(1, len(os.listdir(third_path)))
        odd_num = random.randint(1, len(os.listdir(odd_path)))
       
        if same_folder:
            while (num1 == num2) or (num1 == num3) or (num3 == num2):
                num1 = random.randint(1, len(os.listdir(first_path)))
                num2 = random.randint(1, len(os.listdir(second_path)))
                num3 = random.randint(1, len(os.listdir(third_path)))
        
        im1 = Image.open(first_path + '/img_' + str(num1) + '.jpg')
        im2 = Image.open(second_path+ '/img_' + str(num2) + '.jpg')
        im3 = Image.open(third_path + '/img_' + str(num3) + '.jpg')
        odd = Image.open(odd_path + '/img_' + str(odd_num) + '.jpg')
           
        if n < 8:
            count1 = len(os.listdir(dataset+'/1')) + 1
            label_path = dataset+'/1/'+str(count1)
                        
            if not os.path.exists(label_path):
                os.mkdir(label_path)
                       
            odd.save(label_path+'/1.jpg')
            im1.save(label_path+'/2.jpg')
            im2.save(label_path+'/3.jpg')
            im3.save(label_path+'/4.jpg')
        
        if n >= 8 and n < 16:
            count2 = len(os.listdir(dataset+'/2'))  + 1
            label_path = dataset+'/2/'+str(count2)
                        
            if not os.path.exists(label_path):
                os.mkdir(label_path)
                       
            im1.save(label_path+'/1.jpg')
            odd.save(label_path+'/2.jpg')
            im2.save(label_path+'/3.jpg')
            im3.save(label_path+'/4.jpg')
        
        if n >= 16 and n < 24:
            count3 = len(os.listdir(dataset+'/3'))  + 1
            label_path = dataset+'/3/'+str(count3)
                        
            if not os.path.exists(label_path):
                os.mkdir(label_path)
                       
            im1.save(label_path+'/1.jpg')
            im2.save(label_path+'/2.jpg')
            odd.save(label_path+'/3.jpg')
            im3.save(label_path+'/4.jpg')
            
        if n >= 24:
            count4 = len(os.listdir(dataset+'/4')) + 1
            label_path = dataset+'/4/'+str(count4)
                        
            if not os.path.exists(label_path):
                os.mkdir(label_path)
                       
            im1.save(label_path+'/1.jpg')
            im2.save(label_path+'/2.jpg')
            im3.save(label_path+'/3.jpg')
            odd.save(label_path+'/4.jpg')
            
from PIL import Image
import os

path = '/home/rebecca/Desktop/AIML_working_area/dataset_5'

dim = 224

for category in os.listdir(path):
    count = 1
    for folder in os.listdir(path + '/' + category):
        
        img1 = path + '/' + category + '/' +folder+ '/1.jpg'
        img2 = path + '/' + category +'/' +folder+ '/2.jpg'
        img3 = path + '/' + category + '/' +folder+'/3.jpg'
        img4 = path + '/' + category + '/' +folder+'/4.jpg'
        
        image1 = Image.open(img1)
        image2 = Image.open(img2)
        image3 = Image.open(img3)
        image4 = Image.open(img4)
        
        image1.thumbnail((dim, dim))
        image2.thumbnail((dim, dim))
        image3.thumbnail((dim, dim))
        image4.thumbnail((dim, dim))
        
        image1.save(img1)
        image2.save(img2)
        image3.save(img3)
        image4.save(img4)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 22:59:37 2020

@author: rebecca
"""

import os

path = '/home/rebecca/Desktop/ML_project/clipart'

for category in os.listdir(path):
    count = 1
    for img in os.listdir(path + '/' + category):
        src = path + '/' + category + '/'
        os.rename(src + img, src + 'img_' + str(count) + '.jpg')
        count = count + 1
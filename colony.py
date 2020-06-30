#!/usr/bin/env python

import pandas as pd
import numpy as np
from PIL import Image

file_path = 'D.xlsx'
image_path = 'D.jpg'

df = pd.read_excel(file_path)
im = Image.open(image_path)

def cropColony(row,im):
    '''Crop the bottom half-ish of colony
    '''
    left = row['X'] - row['Width']/4
    upper = row['Y']
    height = row['Height']/3
    width = row['Width']/2
    right = left + width
    lower = upper + height
    cropim = im.crop((left,upper,right,lower))
    return cropim

def averageRGB(image):
    '''Calculate average RGB (each) of image
    '''
    npim = np.array(image)
    # get shape
    w,h,d = npim.shape
    # change shape
    npim.shape = (w*h,d)
    # get average
    return np.round(npim.mean(axis=0),2)

df['CropIm'] = df.apply(lambda x: cropColony(x,im),axis=1)
df['average_RGB'] = df.apply(lambda x: averageRGB(x['CropIm']),axis=1)

RGB_array = np.stack(df['average_RGB'].values,axis=0)
pd.DataFrame(RGB_array,columns=['R','G','B']).to_excel('average_RGB.xlsx')

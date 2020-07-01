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

def get_round_colony_area():
    # select colony items with high roundness
    # return area value of that item in a array? avg? stdev?
    return None

def remove_conjoined_colonies():
    # find items that have relatively low roundness but relatively round get_round_colony_area
    # and remove thme from df
    return None

df['CropIm'] = df.apply(lambda x: cropColony(x,im),axis=1)
df['CropImSize'] = [x.size[0]*x.size[1] for x in df['CropIm']]
df['average_RGB'] = [averageRGB(x) for x in df['CropIm']]

RGB_array = np.stack(df['average_RGB'].values,axis=0)
pd.DataFrame(RGB_array,columns=['R','G','B']).to_excel('average_RGB.xlsx')

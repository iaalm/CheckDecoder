#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PIL import Image
import urllib.request
from io import BytesIO
from pylab import *

#f = urllib.request.urlopen('http://xk.suda.edu.cn/CheckCode.aspx')
#s = BytesIO(f.read())
s = '2.gif'
im = imread(s,format='gif')
size = (len(im[0]),len(im))
for i in range(size[1]):
    for j in range(size[0]):
        if tuple(im[i,j]) == (0,0,153,255):
            im[i][j] = [0,0,0,255]
        else:
             im[i][j] = [255,255,255,255]
            
img = Image.fromarray(im)

def shadow(mat,shape):
    l = []
    for i in range(shape[1]):
        c = 0
        for j in range(shape[0]):
            if mat[j,i][0] == 0:
                c = c + 1
        l.append(c)
    return l
l = shadow(im,im.shape)
sub = []
last = 0
for i in range(len(l)):
    if l[i] == 0:
        if i - last > 1:
            sub.append(Image.fromarray(im[:,last:i+1]).convert('1'))
        last = i
c = 1
for i in sub:
    subplot(1,4,c)
    c = c + 1
def shadow(mat,shape):
    l = []
    for i in range(shape[0]):
        c = 0
        for j in range(shape[1]):
            if  mat[i,j] == 0:
                c = c + 1
        l.append(c)
    return l
font = []
for img in sub:
    subplot(2,4,c)
    imshow(img)
    minl = 100
    img = img.point(lambda i:255-i)
    for i in range(-10,10):
        t = img.rotate(i,expand=1)
        t = t.point(lambda i:255-i)
        size = t.size
        l = shadow(t.load(),size)
        for i in range(size[0]):
            if l[i] > 0:
                break
        for j in range(size[0] - 1,-1,-1):
            if l[j] > 0:
                break
        if j - i < minl:
            minp = t
            minl = j - i
    font.append(minp)

import os
res = []
for i in font:
    i.convert('RGB').save('tmp.gif')
    os.system('tesseract tmp.gif tmp -psm 10 tesseract_config')
    with open('tmp.txt','r') as f:
        res.append(f.read()[0])
for i in res:
    print(i)


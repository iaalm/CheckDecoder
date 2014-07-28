#!env python3
#-*- coding: utf-8 -*-
import sys
from PIL import Image
import pyocr

def ptoi(name):
	with open(name,'r') as f:
		img = Image.open(name)
	img = img.convert('1')
	img.save('tmp.bmp')
	tools = pyocr.get_available_tools()
	if len(tools) == 0:
		print('No OCR tool found!')
		sys.exit(1)
	print("Using '%s'" % (tools[0].get_name()))
	return tools[0].image_to_string(img)

if __name__ == '__main__':
	print(ptoi('1.gif'))

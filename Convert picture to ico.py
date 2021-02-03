# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 19:52:54 2021

@author: benny
"""


from PIL import Image
filename = 'Benny Horowitz Professional Portrait.jpg'
img = Image.open(filename)
img.save('Horowtiz_Benjamin.ico')
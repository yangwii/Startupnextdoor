# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 15:13:15 2017

@author: yangpengjs
"""

from PIL import Image
from pylab import *
import numpy as np

image = array(Image.open('test.jpg').convert('L'))
print image.shape
print image.flatten().shape

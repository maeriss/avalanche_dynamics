#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 19:35:18 2020

@author: marie
"""

from pylab import loadtxt, figure, imshow, colorbar, savefig, tight_layout, show

zend = loadtxt('zend.txt',unpack=True)

figure(1)
im = imshow(zend,cmap='hot',origin='lower')
colorbar(im)
savefig('zend.png')
tight_layout()

show()
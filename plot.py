#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 18:09:32 2020

@author: marie
"""

from pylab import loadtxt, figure, plot, xlabel, ylabel, tight_layout, savefig, show
from data import *


res = loadtxt('bak.txt',unpack=True)

t = res[0]
r = res[1]
s = res[2]
zsom = res[3]
n = 5
zc = 4



figure(1)
plot(t,r,'k-')
xlabel('temps',fontsize=12)
ylabel('nbre de redistribution locales r',fontsize=12)
tight_layout()
savefig('r_t.png')


figure(2)
plot(t,s,'k-')
xlabel('temps',fontsize=12)
ylabel('nbre de grains sortis s',fontsize=12)
tight_layout()
savefig('s_t.png')


figure(3)
plot(t,zsom)
xlabel('temps',fontsize=12)
ylabel(r'somme des z(i,j) Z',fontsize=12)
tight_layout()
savefig('zsom_t.png')

figure(4)
zmax = n*n*zc
plot(t,zsom/zmax)
xlabel('temps',fontsize=12)
ylabel(r'Z/Zmax',fontsize=12)
tight_layout()
savefig('zmax_t.png')



show()
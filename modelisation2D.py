#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 17:50:27 2020

@author: marie
"""

import os
from pylab import loadtxt, savetxt
from numpy import random
from numpy import sum as npsum

from data import *

def relax(z,zc,t,file=False):     #z is the zend.txt with the previous slopes in an array shape
                                  #zc is the critical slope, t is the time "stamp"
  s = 0       #counts the number of slopes index that fall in the ravine
  r = 0       #number of relaxations (i.e of positions which were instable)

  nx = z.shape[0]     #takes the txt with slopes stored and counts the number of lines
  ny = z.shape[1]     #sames for columns

  move = True
  iav = []      #to store i positions where slopes are critical or higher
  jav = []      #same for j positions

  while(move):     #as long as there are critical slopes, we relax, else the loop ends
    move = False

    for i in range(nx):       #browsing lines...
      for j in range(ny):     #... and on columns (to check every position possible)
        if (z[i,j] > zc):     #if the position in i,j is higher than zc
          r += 1
          move = True           #put move to True, to check if the instability of i,j will create another one or not
          z[i,j] -= 4           #the position looses 4 in slope
          if ((i+1)<=(nx-1)):   #if the slope on the right of the position is not on the right edge...
            z[i+1,j] += 1       #... then it gains 1 slope index normally
          else:
            s += 1              #otherwise (i.e. the position on the right is on the edge), it falls in the ravine
          if ((i-1)>=0):        #same thing but on the left edge
            z[i-1,j] += 1
          else:
            s += 1
          if ((j+1)<=(ny-1)):   #same thing on the bottom edge...
            z[i,j+1] += 1
          else:
            s += 1
          if ((j-1)>=0):        #... and on the top edge
            z[i,j-1] +=1
          else:
            s += 1
          iav.append(i)         #we store the position (i,j) in respective tabs
          jav.append(j)

  if len(iav)>0 and file:       #if there was at least one instable position
    file.write(str(t)+'\n')     #we store the timestamp when it happened
    file.write(' '.join(str(i) for i in iav))   #then the position i
    file.write('\n')
    file.write(' '.join(str(j) for j in jav))   #and the position j
    file.write('\n')

  return z,r,s        #return new slopes after relaxation, s nbr of fallen slopes, r number of relaxation


#________________________________________________________________
if __name__ == '__main__':
#________________________________________________________________

  n=50
  z0=10
  tmax = 10
  zc = 4
  tstore = [0,1,6,8]


  #initialization of the tab with random vairables
  z = random.rand(n,n)*z0
  z = z.astype(int)    #put all datas of the z array in int

  #or we start with a previous result stored in zend.txt
  if (os.path.isfile('zend.txt')):
    z = loadtxt('zend.txt',unpack=True,dtype=int)


  #create the storage files
  of = open('bak.txt','w')
  of.write('#temps nbre_relax nbre_sortis\n')

  of2 = open('avalanches.txt','w')
  of2.write('# les n avalanches sont stockées de la façon suivante\n')
  of2.write('# ligne n : temps\n')
  of2.write("# ligne n+1 : abscisses i des grains de l'avalanche\n")
  of2.write("# ligne n+2 : prdonnées j des grains de l'avalanche\n")

  #boucle temps
  for t in range(tmax):

    #perturbation localisée : on génère une position aléatoire et on rajoute un grain à cet endroit
    pos = random.rand(2)*(n-1)
    z[int(pos[0]),int(pos[1])] += 1

    #relaxation du tas
    if t in tstore:     #à changer en < tmax? c'est quoi tstore?
      z,r,s = relax(z,zc,t,file=of2)
    else:
      z,r,s = relax(z,zc,t)

    #pente totale
    zsom = npsum(z)

    print(t,r,s,zsom)
    of.write('{0:4d} {1:4d} {2:4d} {3:4d}\n'.format(t,r,s,zsom))

  of.close()
  of2.close()
  savetxt('zend.txt',z,fmt='%1d',header='distribution finale')



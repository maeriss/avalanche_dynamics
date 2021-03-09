#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 15:43:13 2020

@author: marie
"""

import random
import matplotlib.pyplot as plt
from copy import deepcopy

tmax=5
t=0

def montain(n):
  L=[6]
  for i in range(n-1):
    L+=[random.randint(1,6)]
  return L

mont=montain(5)
print(mont)


def itsnows(mont):
  k=random.choice(mont)
  pos=mont.index(k)
  mont[pos]+=1
  return mont


def instable(mont):
  colins=[]
  for i in range(len(mont)-1):
    if mont[i]-mont[i+1]>2:
      colins+=[i]
    elif mont[i]-mont[i+1]<-2:
      colins+=[i+1]
  if mont[len(mont)-1]>2:
    colins+=[len(mont)-1]
  return colins


def simple(colins):
  col=[]
  for elt in colins:
    if elt not in col:
      col+=[elt]
  return col


def relaxation(mont):
  colo=instable(mont)
  co=simple(colo)
  T=0
  for i in co:
    if i!=len(mont)-1:
      mont[i]+=(-2)
      mont[i+1]+=2
    else:
      mont[i]+=(-2)
      T=T+2
  t=[T]
  final=[mont,t]
  return final


def trace(mont):
  colins=instable(mont)
  col=simple(colins)
  y1=deepcopy(mont)
  y2=[]
  for k in range(len(mont)):
    y2+=[0]
  for i in col:
    y1[i]+=(-2)
    y2[i]+=2
  r=range(len(y1))
  plt.bar(r,y1,width=1,color=['white' for i in y1],edgecolor=['black' for i in y1])
  plt.bar(r,y2,width=1,bottom=y1,color=['black' for i in y1],edgecolor=['black' for i in y1])
  plt.grid(axis='y',alpha=0.75)
  plt.show()
  return mont


def relaxtot(mont):
  colins=instable(mont)
  col=simple(colins)
  fallen=[]
  while col!=[]:
    trace(mont)
    final=relaxation(mont)
    fallen=fallen+final[1]
    colins=instable(mont)
    col=simple(colins)
  ravin=sum(fallen)
  trace(mont)
  return mont,ravin


while t<tmax:
  mont = itsnows(mont)
  print(mont)
  print(relaxtot(mont))
  t+=1


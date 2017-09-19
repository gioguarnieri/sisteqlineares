#!/usr/bin/env python
from random import randint
import numpy as np

for i in xrange(3,10):
 filewrite=open("matriz"+str(i)+".dat", 'w')
 x=np.zeros((i,i), float)
 for tt in xrange(0,i):
  for t in xrange(0,i+1):
   filewrite.write(str(randint(0,9))+"  ")
  filewrite.write("\n") 
 filewrite.close()

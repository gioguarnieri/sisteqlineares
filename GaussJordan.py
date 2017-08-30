#!/usr/bin/env python
#1  1  0  3  4
#2  1 -1  1  1
#3 -1 -1  2 -3
#-1 2  3 -1  4

import sys
import numpy as np
x=np.matrix( ((1.,1.,0.,3.,4.), (2.,1.,-1.,1.,1.), (3.,-1.,-1.,2.,-3.), (-1.,2.,3.,-1.,4.)) )
n=len(x)-1
print "Matriz antes de tudo:"
print x
for i in xrange(n,-1,-1):
 for ii in xrange(n,-1,-1):
  if(x.item(i,ii)==0):
   y=np.copy(x[ii+1])
   x[ii+1]=np.copy(x[i])
   x[i]=np.copy(y)
print "Matriz ordenada: "
print x



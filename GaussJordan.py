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

for i in xrange(1,n+1):
 x[i]=np.copy(x[i]-x[0]*(x.item(i,0)/x.item(0,0)))

print "Matriz com primeira coluna zerada"
print x

print "Comecando o escalonamento"
for tt in xrange(0, n):
 for t in xrange(tt+1,n+1):
  if x.item(t,tt)!=0:
   x[t]=np.copy(x[t]-x.item(t,tt)/x.item(tt,tt)*x[tt])

print "Matriz final"
print x

y=np.zeros([n+1], float)
for i in xrange(0,n+1):
 y[i]=x.item(i,n+1)

for i in xrange(n,-1,-1):
 j=n
 while (j>i):
  y[i]=y[i]-x.item(i,j)*y[j]
  j=j-1
 y[i]=y[i]/x.item(i,i)
print "Valores finais da substituicao:"
print y


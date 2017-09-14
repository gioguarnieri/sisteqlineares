#!/usr/bin/env python
#1  1  0  3  4
#2  1 -1  1  1
#3 -1 -1  2 -3
#-1 2  3 -1  4

#2  2 -1  3
#3  3  1  7
#1 -1  5  5

import sys
import numpy as np

def Escalona(x):
 moddet=0
 for tt in xrange(0, n):
  for t in xrange(tt+1,n+1):
   if abs(x.item(tt,tt))<abs(x.item(t,tt)):
    moddet=moddet+1
    y=np.copy(x[tt])
    x[tt]=np.copy(x[t])
    x[t]=np.copy(y)
   x[t]=np.copy(x[t]-x.item(t,tt)/x.item(tt,tt)*x[tt])
 return x, moddet

def CalculoDet(x):
 det=1
 for i in xrange(0,n+1):
  det=det*x.item(i,i)
 det=det*(-1)**moddet
 return det

def Substitui(x):
 y=np.zeros([n+1], float)
 for i in xrange(0,n+1):
  y[i]=x.item(i,n+1)
 
 for i in xrange(n,-1,-1):
  j=n
  while (j>i):
   y[i]=y[i]-x.item(i,j)*y[j]
   j=j-1
  y[i]=y[i]/x.item(i,i)
 return y

def Coeficientes(x):
 w=np.zeros([n+1], float)
 for tt in xrange(0,n+1):
  for t in xrange(0,n+1):
   w[tt]=np.copy(w[tt]+y[t]*z.item(tt,t))
 return w


fileread=open(sys.argv[1], 'r')
l=[ line.split() for line in fileread ]
for i in xrange(0, len(l)):
 for ii in xrange(0,len(l)+1):
  l[i][ii]=float(l[i][ii])

x=np.matrix(l)


z=np.copy(x)
n=len(x)-1
print "Matriz antes de tudo:"
print x
#for i in xrange(n,-1,-1):
# for ii in xrange(n,-1,-1):
#  if(x.item(i,ii)==0):
#   y=np.copy(x[ii+1])
#   x[ii+1]=np.copy(x[i])
#   x[i]=np.copy(y)
#print "Matriz ordenada: "
#print x

#for i in xrange(1,n+1):
# x[i]=np.copy(x[i]-x[0]*(x.item(i,0)/x.item(0,0)))

#print "Matriz com primeira coluna zerada"
#print x
moddet=0
print "Comecando o escalonamento"
x,moddet=Escalona(x)

print "Matriz final"
print x

det=CalculoDet(x)
print "Valor do determinante:"
print det

y=Substitui(x)

simply=[ round(elem,2) for elem in y ]

print "Valores finais do escalonamento:"
print simply

w=Coeficientes(x)
print "Valores depois de substituir nos coeficientes: "
print w



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


def Ler(x):
 resp=[]
 fileread=open(sys.argv[1], 'r')
 l=[ line.split() for line in fileread ]
 for i in xrange(0, len(l)):
  for ii in xrange(0,len(l)+1):
   l[i][ii]=float(l[i][ii])
 for i in xrange(0,len(l)):
  resp.append(l[i][len(l)])
  l[i].pop(len(l))
 x=np.matrix(l)
 return x, resp




def Escalona(x,resp):
 lu=np.zeros((n+1,n+1), float)
 resp2=np.zeros(n, float)
 resp2=resp
 lamda=[]
 moddet=0
 op=0
 for tt in xrange(0, n):
  for t in xrange(tt+1,n+1):
   #if abs(x.item(tt,tt))<abs(x.item(t,tt)):
   # moddet=moddet+1
   # y=np.copy(x[tt])
   # x[tt]=np.copy(x[t])
   # x[t]=np.copy(y)
   op=op+2+n
   lamda.append(x.item(t,tt)/x.item(tt,tt))
   resp2[t]=resp2[t]-lamda[-1]*resp2[tt]
   x[t]=np.copy(x[t]-lamda[-1]*x[tt])
   lu.itemset((t,tt),lamda[-1])
 for i in xrange(0,n+1):
  lu.itemset((i,i),1)
 return x,moddet,lamda,op,resp2,lu



def CalculoDet(x):
 det=1
 for i in xrange(0,n+1):
  det=det*x.item(i,i)
 det=det*(-1)**moddet
 return det



def Substitui(x,resp2):
 y=resp2
 for i in xrange(n,-1,-1):
  j=n
  while (j>i):
   y[i]=y[i]-x.item(i,j)*y[j]
   j=j-1
  y[i]=y[i]/x.item(i,i)
 return y



def Coeficientes(z,y):
 w=np.zeros([n+1], float)
 for tt in xrange(0,n+1):
  for t in xrange(0,n+1):
   w[tt]=np.copy(w[tt]+y[t]*z.item(tt,t))
 return w


x=0
x,resp=Ler(x)
lu=np.zeros((len(x)+1,len(x)+1), float)

z=np.copy(x)
n=len(x)-1
print "Matriz antes de tudo:"
print x

print "Parametros: "
print resp

moddet=0
print "Comecando o escalonamento"
x,moddet,l,op,resp2,lu=Escalona(x,resp)

print "Matriz L"
print lu

print "Matriz U"
print x

print "LxU"
print lu*x 

print "LxU e igual a matriz original?"
print lu*x==z

det=CalculoDet(x)
print "Valor do determinante:"
print det

y=Substitui(x,resp2)

simply=[ round(elem,2) for elem in y ]

print "Valores finais do escalonamento:"
print simply

w=Coeficientes(z,y)
print "Valores depois de substituir nos coeficientes: "
print w

print "Quantidade de operacoes: "
print op
filewrite=open("graph.dat", "a")
filewrite.write(str(len(x))+' '+str(op)+'\n')


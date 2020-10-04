import math 
s=1
n=1.0
t= 1.0
pi = 0 
while math.fabs(t) >= 1e-6:
 pi = pi+t
 n=n+2
 s=-s
 t =s/n
pi =pi * 4
print("PI =%f"%pi)

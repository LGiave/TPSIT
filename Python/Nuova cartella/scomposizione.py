N=564647658576346364534563636465346756779898756362
d=2
scomposizione=str(N)+"="
while N>=d:
  if N%d == 0:
     scomposizione=scomposizione+'*'+str(d)
     N=N/d
  else:
   d=d+1

print(scomposizione)
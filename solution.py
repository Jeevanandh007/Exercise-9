def f8(f,m):
  s=0

  with open(f,'r') as f:
    factors = [int(line.strip()) for line in f]
  with open(m,'r') as m:
    multiples = [int(line.strip()) for line in m]

  s=sum(i for i in multiples if any (i%j==0 for j in factors))
  return s

myList=list(range(1000))
myList.pop(168)
with open('multiples','w') as y:
  for x in myList:
    y.write(str(x)+'\n')
with open('factors','w') as y:
  for x in [3,5,991]:
    y.write(str(x)+'\n')
f8('factors','multiples')==233991

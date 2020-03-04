

#n = int(input())
#m = int(input())

n=7
m=21


graphic1 = '.|.'

n_chop = int(n/2)
m_chop = int(m/2)+1

for i in range(0,n_chop):
   print((graphic1*(i*2+1)).center(int(m), '-'))
   
print('WELCOME'.center(m,'-'))

for i in range(n_chop, 0, -1):
   print((graphic1*(i*2-1)).center(m, '-'))
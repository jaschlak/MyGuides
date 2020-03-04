
#If I cared I would make the logic better

n = 23

letstring = 'abcdefghijklmnopqrstuvwxyz'

# build middle string
mid_string = ''
for i in range(n-1, 0, -1):
    mid_string += letstring[i] + '-'
    

for i in range(0, n):
    mid_string += letstring[i] + '-'
mid_string = mid_string[:-1]


#build vertical strings

half_string = mid_string[int(len(mid_string)/2):]

for i in range(0,n):

    new_string = half_string[len(half_string)-1-i*2:][1:][::-1] + half_string[len(half_string)-1-i*2:]
    print(new_string.center(len(mid_string),'-'))
    
for i in range(n-2,-1,-1):
    new_string = half_string[len(half_string)-1-i*2:][1:][::-1] + half_string[len(half_string)-1-i*2:]
    print(new_string.center(len(mid_string),'-'))

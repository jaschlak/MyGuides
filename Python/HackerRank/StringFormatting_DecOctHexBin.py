
n = 17

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
        
    array = digits[::-1]
    string = ''
    for char in array:
        string+=str(char)
    
    return string


def dec2hex(d):
    string = hex(d).split('x')[-1]
    return string.upper()


spacing = len(numberToBase(n, 2))

for i in range(1,n+1):
    
    # decimal
    i_dec = str(i)
    string = i_dec.rjust(spacing+1)
    
    # octal
    i_octal = numberToBase(i, 8)
    string += i_octal.rjust(spacing+1)
    
    # hex
    i_hex = dec2hex(i)
    string += i_hex.rjust(spacing+1)
    
    # bin
    i_bin = numberToBase(i, 2)
    string += i_bin.rjust(spacing+1)
    
    print(string)

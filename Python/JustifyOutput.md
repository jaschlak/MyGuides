# Justify Output

    Print output at the same start point in the middle of variable text
    
## Code:


import random

# makes randome words
def create_random_word(n):
    
    import urllib.request

    word_url = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
    response = urllib.request.urlopen(word_url)
    long_txt = response.read().decode()
    words = long_txt.splitlines()

    return words

# Get random words
words = create_random_word(10)

# prints them all together
for word in words[0:10]:
    
    word = word + ': '
    string = word.rjust(20, '-') + 'jamba_juice'
    print(string)
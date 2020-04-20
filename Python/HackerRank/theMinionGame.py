
import re



string = 'Banana'

string = string.upper()

vowels = 'A E I O U'.split()



# %%

# returns unique characters from string
def unique(string):

    unique_string = ''    
    for item in string:
        if item not in unique_string:
            unique_string += item
    return unique_string

# adds up points based on finding a pattern in a string
def points(pat, string):
    
    count = 0
    
    for i in range(0,len(string)):
        if re.search('^' + pat, string[i:]):
            count += 1
            
    return count
    
def try_all(start, list1, list2):
    
    pat = '^' + start
    
    for i in range(9,len(list1)):
        re_find_start = re.search(pat,list1[i:])
        if re_find_start:
            break
    
    print(re_find_start)

# %%
# split vowels and consenents
word_vowl = ''
word_cons = ''

for item in string:
    if item in vowels:
        word_vowl += item
        
    else:
        word_cons += item
        
# Stuart
#print(word_vowl)

# Kevin
#print(word_cons)


# %% 

unique_vowl = unique(word_vowl)
unique_cons = unique(word_cons)

print(unique_vowl)
print(unique_cons)
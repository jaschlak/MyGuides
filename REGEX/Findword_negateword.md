# Find word, negate other word

    Find all lines containing one word and negate another word
    
## Code:

    ^(?!.*<negate word>).*<contains word>.* 
    
## Multiple inputs:

    ^(?!.*<1st negate word>|<2nd negate word>).*<contains word>.* 
    
## Example code

    ^(?!.*socket).*error.*                                                  Finds word "error", but wont report if the word "socket" is in the line
    
Note: you can add a $ to the end to close the search bar
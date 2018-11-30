# Find word, negate other word

    Find all lines containing one word and negate another word
    
## Code:

    ^(?!.*<negate word>).*<contains word>.*
    
## Example code

    ^(?!.*socket).*error.*
    
Note: you can add a $ to the end to close the search bar
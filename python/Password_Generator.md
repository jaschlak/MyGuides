# Password Generator

    This creates a random password based on the values you allow to be used
    
## Code:

    import random

    #%% Open and read file

    char_string = r"A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c" + \
    " d e f g h i j k l m n o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9 ` - = ]" + \
    " [ ' ; / . , ~ ! @ # $ % ^ & * ( ) _ _ + | } { \" : ? > <"

    char_list = char_string.split(' ');

    pass_len = 5

    password = ''

    for i in range(0,pass_len):
        password = password + char_list[random.randint(0,len(char_list)-1)]
        
    print(password)
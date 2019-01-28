# Reading and Writing to .txt

    Different operations that can be used to work with your .txt files
    
## Check if .txt file exists, if it does not then create and empty file

    file = '<filename.txt>';

    if not os.path.exists(file):
        f=open(file,"w+")
        f.close()
        
## Read .txt file:

    txt_con = open(file,"r")
    file=txt_con.read()
    txt_con.close()

    
## Overwrite .txt file

    text = 'sometext'

    txt_con= open(file,"w")
    txt_con.write(text)
    txt_con.close()
    
## Append .txt file without going to a new line (add \n if you want to)

    text = 'This is new text and wont go to a new line'

    txt_con= open(file,"a+")
    txt_con.write(text)
    txt_con.close()

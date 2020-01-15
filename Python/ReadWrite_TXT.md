# Reading and Writing to .txt

    Different operations that can be used to work with your .txt files
    
## Check if .txt file exists, if it does not then create and empty file

    filename = '<filename.txt>'

    if not os.path.exists(filename):
        file=open(filename,"w")
        file.close()
    
## Overwrite .txt file

    text = '<insert some text>'

    file= open(filename,"w")
    file.write(text)
    file.close()
    
## Append .txt file without going to a new line (add \n if you want to)

    text = '\nThis is new text and wont go to a new line'

    file= open(filename,"a+")
    file.write(text)
    file.close()


## Read entire .txt file:

    file = open(filename,"r")
    txt_cont=file.read()
    file.close()
    
## Read linebyline from .txt file:

    file = open(filename,"r")
    text_cont = file.readline()
    file.close
    
## Read entire file linebyline from .txt
    
    def read_file_linexline(filename):
        
        file = open(filename,"r")
        
        line =  file.readline()
        cnt = 1
        
        while line:
            print(line.strip())
            line = file.readline()
            cnt +=1
        
        file.close
    
## Read entire txt document as DataFrame

    df = pd.read_fwf(path, widths = [1000])                     # widths is a list of how long you want each column to be, this example makes a single column
    or
    df = pd.read_csv(log_path + '/' + log_list[0], header=None, sep='\s!!!\t\s', engine='python')
    

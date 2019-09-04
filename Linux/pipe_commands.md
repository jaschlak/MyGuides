# Piping Commands

    Piping commands into each other, may want to revise second and third method after more use
    
# Methods

    ls | grep "<enter filter>                   Normal Piping, can't handle new commands
    
    
    <command1> -exec <command2> {results of command1} \;
    find . -name '*' -exec file {} \;                               # pipes list of files here into file commands
    
    <command2> `<command1>`
    file `ls`                                                       # method 2, note ` is a backtick, doesn't work if filename has spaces
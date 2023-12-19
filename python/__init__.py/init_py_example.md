
# __init__.py example

    This is an example of how to use an __init__.py with modular libraries that use the same names
    
## Structure

    root folder
    |- folder1
    |  |- __init__.py
    |  |- program.py
    |  |-resource
    |      |-print_file.py
    |- folder2
    |  |- __init__.py
    |  |- program.py
    |  |-resource
    |      |-print_file.py
    |-main.py
    
    
## main.py contents

    from folder1 import do_print as do_print1
    thing1 = do_print1()

    from folder2.program import do_print as do_print2
    thing2 = do_print2()

## folder1.__init__.py contents

    from folder1.program import do_print
    
## folder1.program.py contents

    from folder1.resource.print_file import  print_stuff

    def do_print():
        print_stuff()

    if __name__ == '__main__':
        do_print()
        
## folder1.resource.print_file.py contents

    from pathlib import Path

    def print_stuff():
        print(Path(__file__).resolve())
        
## folder2.__init__.py contents

    from folder2.program import do_print
    
## folder2.program.py contents

    from folder2.resource.print_file import  print_stuff

    def do_print():
        print_stuff()

    if __name__ == '__main__':
        do_print()
        
## folder2.resource.print_file.py contents

    from pathlib import Path

    def print_stuff():
        print(Path(__file__).resolve())
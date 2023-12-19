# Getting CMD Output

    This is a simple python code for getting CMD output from a command
    
## Code:

    import subprocess

    p = subprocess.Popen('sc query vx.appserver', stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    print(p.stdout.read())
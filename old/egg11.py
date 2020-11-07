import sys


for line in sys.stdin:
    line = line.rstrip()
    
    if line:         
        try:
            b = int(line, base=2)
            if b % 3 == 0:
                print(line)
        except ValueError:
            pass
    else:
        break
    

    

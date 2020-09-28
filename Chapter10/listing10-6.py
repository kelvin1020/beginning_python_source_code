# numberlines.py                              
                                              
import fileinput                              
                                              
for line in fileinput.input(inplace=True):    
    line = line.rstrip()                      
    num  = fileinput.lineno()                
    print ('%-45s # %2i' % (line, num))      

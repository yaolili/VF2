#-*- coding:utf-8 -*-
# AUTHOR:   yaolili
# FILE:     run.py
# ROLE:     run vf.py
# CREATED:  2015-12-2 21:34:15

import os
import sys
import time
from vf import Vf

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print "sys.argv[1]: Graph file"
        print "sys.argv[2]: subGraph file"
        print "sys.argv[3]: output file"
        exit()
    
    start = time.clock()    
    output = open(sys.argv[3], 'w+')
    sys.stdout = output
    
    vf2 = Vf()   
    vf2.main(sys.argv[1], sys.argv[2])   
    
    end = time.clock()
    print "time: ", (end - start)/60
    output.close()

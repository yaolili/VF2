#-*- coding:utf-8 -*-
# AUTHOR:   yaolili
# FILE:     run.py
# ROLE:     TODO (some explanation)
# CREATED:  2015-12-2 21:34:15

import os
import sys
from vf import Vf

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print "sys.argv[1]: Graph file"
        print "sys.argv[2]: subGraph file"
        print "sys.argv[3]: output file"
        exit()
    
    vf2 = Vf()
    vf2.main(sys.argv[1], sys.argv[2], sys.argv[3])   
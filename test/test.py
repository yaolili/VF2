#-*- coding:utf-8 -*-
# AUTHOR:   yaolili
# FILE:     test.py
# ROLE:     TODO (some explanation)
# CREATED:  2015-11-28 20:55:11
# MODIFIED: 2015-11-30 20:10:39

import os
import sys
from graph import GraphSet
from map import Map

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print "sys.argv[1]: Graph file"
        print "sys.argv[2]: subGraph file"
        exit()
       
    input = GraphSet(sys.argv[1])
    #print input.curGraph(1)
    print "VSet: ", input.curVSet(1)
    print "ESet: ", input.curESet(1)
    print "VESet: ", input.curVESet(1)
    print "graph neighbor: ", input.neighbor(1, 1)
    result = {}
    curMap = Map(result)
    print "isCovered: ", curMap.isCovered(input.curVESet(1))
    neighbor = curMap.neighbor(1, input, 1)
    print "map neighbor: ",neighbor
    
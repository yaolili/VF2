#-*- coding:utf-8 -*-
# AUTHOR:   yaolili
# FILE:     test.py
# ROLE:     TODO (some explanation)
# CREATED:  2015-11-28 20:55:11
# MODIFIED: 2015-11-28 20:55:11

import sys
import os


def readGraph(inputFile):
    lineNum = -1
    subGraphSet = []
    try:
        with open(inputFile, "r") as fin:
            vertexSet = {}
            edgeSet = {}
            for line in fin:
                lineList = line.strip().split(" ")
                if not lineList:
                    print "ReadGraph line split error!"
                    exit()
                #A new subGraph!
                if lineList[0] == 't':
                    #Write it to subGraphSet
                    if lineNum > -1:
                        currentSubGrap = (lineNum, vertexSet, edgeSet)
                        subGraphSet.append(currentSubGrap)
                    lineNum += 1
                    vertexSet = {}
                    edgeSet = {}
                elif lineList[0] == 'v':
                    if len(lineList) != 3:
                        print "ReadGraph line vertex error!"
                        exit()
                    vertexSet[lineList[1]] = lineList[2]
                else:
                    #lineList[0] == 'e'
                    if len(lineList) != 4:
                        print "ReadGraph line edge error!"
                        exit()
                    edgeKey = str(lineList[1]) + ":" + str(lineList[2])
                    edgeSet[edgeKey] = lineList[3]
        return subGraphSet            
    except IOError, e:
        print "Cannot open Graph file: ", e
        exit()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "sys.argv[1]: Graph file"
        exit()
    
    graphSet = readGraph(sys.argv[1])
    print graphSet
    print type(graphSet)
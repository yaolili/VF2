#-*- coding:utf-8 -*-
# AUTHOR:   yaolili
# FILE:     test.py
# ROLE:     TODO (some explanation)
# CREATED:  2015-11-28 20:55:11
# MODIFIED: 2015-11-30 20:10:39

import sys
import os

graphSet = []
subGraphSet = []

def vertexEdgeSet(vertexNum, edgeSet):
    if not (vertexNum and edgeSet):
        print "vertexEdgeSet() arguments error! vertexNum or edgeSet is empty!"
        exit()
    #define two dimensional array
    #notice, here you can't use like this: result = [[]] * vertexNum
    result = [[] for i in range(vertexNum)]
        
    for key in edgeSet:
        v1, v2 = key.strip().split(":")
        #print int(v1)
        #print int(v2)
        result[int(v1)].append(key)
        result[int(v2)].append(key)
    return result


 
def neighborSet(mapGraph, graphVertexSet, graphEdgeSet):
    #notice, mapGraph can be empty and type can be 0!
    if not (graphVertexSet):
        print "neighborSet() arguments error! graphVertexSet is empty!"
        exit()
        
    graphVertexNum = len(graphVertexSet)          
    VES = vertexEdgeSet(graphVertexNum, graphEdgeSet)
    
    neighborVertexSet = []
    for index in mapGraph:
        aList = VES[int(index)]
        for i in range(len(aList)):
            v1, v2 = aList[i].strip().split(":")
            if v1 != index:
                if v1 not in (neighborVertexSet and mapGraph):
                    neighborVertexSet.append(v1)
            elif v2 != index:
                if v2 not in (neighborVertexSet and mapGraph):
                    neighborVertexSet.append(v2)
            else:
                print "VES wrong!"
                exit()

    #unconnected graph! or init process!
    if not neighborVertexSet:
        for index in graphVertexSet:
            if index not in mapGraph:
                neighborVertexSet.append(index)    
    #print "in neighborSet(), neighborVertexSet: ", neighborVertexSet
       
    return neighborVertexSet
        
    

def isCovered(mapSubGraph, subGraphVertexSet):
    if len(mapSubGraph) == len(subGraphVertexSet):
        return True
    else:
        return False

#return candidate pairs for current state 
def candidate(subGraphNeighbor, graphNeighbor):
    if not (subGraphNeighbor and graphNeighbor):
        print "candidate() arguments error! subGraphNeighbor or graphNeighbor is empty!"
        exit()
    
    '''
    print "in candidate(), subGraphNeighbor: ", subGraphNeighbor
    print "in candidate(), subGraphNeighbor len: ", len(subGraphNeighbor)
    print "in candidate(), graphNeighbor: ", graphNeighbor
    '''
    
    candidatePairs = []
    for i in range(0, len(subGraphNeighbor)):
        for j in range(0, len(graphNeighbor)):
            candidateString = str(subGraphNeighbor[i]) + ":" + str(graphNeighbor[j])
            candidatePairs.append(candidateString)
    return candidatePairs

def preSucc(n, VES, result):
    aList = VES[n]
    for i in range(len(aList)):
        v1, v2 = aList[i].strip().split(":")
        if v1 != index:
            if v1 not in result.keys():
        elif v2 != index:
            if v2 not in (neighborVertexSet and mapGraph):
        else:
            print ""

#meet feasibility rules or not, return true or false
def isMeetRules(n, m, result, graphVertexSet, graphEdgeSet, subGraphVertexSet, subGraphEdgeSet):
    #label match failure 
    if(s
    ubGraphVertexSet[n] != graphVertexSet[m]):
        return False
        
    subGraphVertexNum = len(subGraphVertexSet)
    subVES = vertexEdgeSet(subGraphVertexNum, subGraphEdgeSet)
    graphVertexNum = len(graphVertexSet)          
    gVES = vertexEdgeSet(graphVertexNum, graphEdgeSet)
    
    
    for i in range(len(aList)):
        v1, v2 = aList[i].strip().split(":")
            if v1 != index:
                if v1 not in (neighborVertexSet and mapGraph):
                    neighborVertexSet.append(v1)
            elif v2 != index:
                if v2 not in (neighborVertexSet and mapGraph):
                    neighborVertexSet.append(v2)
            else:
                print "VES wrong!"
                exit()
    
    
    return True

#main entrance, return match data structures 
def dfsMatch(currentSubGraph, currentGraph, result):
    #notice, result can be empty!
    if not (currentSubGraph and currentGraph):
        print "dfsMatch() arguments error! currentSubGraph or currentGraph is empty!"
        exit()      
    
    subGraphVertexSet = currentSubGraph[1]
    subGraphEdgeSet = currentSubGraph[2]       
    graphVertexSet = currentGraph[1]
    graphEdgeSet = currentGraph[2]
    
    mapSubGraph = [] 
    mapGraph = []
    if result:
        for key in result:                        
            mapSubGraph.append(key)
            mapGraph.append(result[key])
    
    if(isCovered(mapSubGraph, subGraphVertexSet)):
        return result
     
    subGraphNeighbor = neighborSet(mapSubGraph, subGraphVertexSet, subGraphEdgeSet)
    graphNeighbor = neighborSet(mapGraph, graphVertexSet, graphEdgeSet)
    
    #mapSubGraph doesn't corver subGraphVertexSet, so subGraphNeighbor and graphNeighbor can't be empty 
    if not (subGraphNeighbor and graphNeighbor):
        print "in dfsMatch(), subGraphNeighbor or graphNeighbor is empty!"
        exit()
    
    #notice, choose one vertex in subGraphNeighbor is ok
    while(len(subGraphNeighbor) > 1):
        subGraphNeighbor.pop()

    #test usage!
    print "in dfsMatch() subGraphNeighbor: ", subGraphNeighbor
    print "in dfsMatch() graphNeighbor: ", graphNeighbor
    print "in dfsMatch() result: ", result
    if len(result) > 1:
        exit()

    candidatePairs = candidate(subGraphNeighbor, graphNeighbor)
    print "in dfsMatch() candidatePairs: ", candidatePairs
    if not candidatePairs:
        return result
                
    for key in candidatePairs:
        v1, v2 = key.strip().split(":")
        #remain to fix
        if(isMeetRules(v1, v2, result, graphVertexSet, graphEdgeSet, subGraphVertexSet, subGraphEdgeSet)):
            
            result[v1] = v2
            print "result aaa: ", result
            dfsMatch(currentSubGraph, currentGraph, result)       
            exit()
            result.pop(key)
    
    return result
        
        
    

#read input file, return graph structures
def readGraph(inputFile):
    if not inputFile:
        print "readGraph() arguments error! inputFile is empty!"
    lineNum = -1
    graphSet = []
    try:
        with open(inputFile, "r") as fin:
            vertexSet = {}
            edgeSet = {}
            for line in fin:
                lineList = line.strip().split(" ")
                if not lineList:
                    print "ReadGraph line split error!"
                    exit()
                #a new graph!
                if lineList[0] == 't':
                    #write it to graphSet
                    if lineNum > -1:
                        currentGraph = (lineNum, vertexSet, edgeSet)
                        graphSet.append(currentGraph)
                    lineNum += 1
                    vertexSet = {}
                    edgeSet = {}
                elif lineList[0] == 'v':
                    if len(lineList) != 3:
                        print "ReadGraph line vertex error!"
                        exit()
                    vertexSet[lineList[1]] = lineList[2]
                elif lineList[0] == 'e':
                    if len(lineList) != 4:
                        print "ReadGraph line edge error!"
                        exit()
                    edgeKey = str(lineList[1]) + ":" + str(lineList[2])
                    edgeSet[edgeKey] = lineList[3]
                else:
                    #empty line!
                    continue
        return graphSet            
    except IOError, e:
        print "Cannot open Graph file: ", e
        exit()

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print "sys.argv[1]: Graph file"
        print "sys.argv[2]: subGraph file"
        exit()
       
    graphSet = readGraph(sys.argv[1])
    subGraphSet = readGraph(sys.argv[2])
    for i in range(len(subGraphSet)):
        currentSubGraph = subGraphSet[i]        
        for j in range(len(graphSet)):
            currentGraph = graphSet[j]
            result = {}        
            result = dfsMatch(currentSubGraph, currentGraph, result)
            #remain to fix
            if len(result) == len(currentSubGraph):
                print "Match! %s %d-th graph isomorphism %s %d-th graph! " %(sys.argv[2], i, sys.argv[1], j)
                print result
                exit()
            else:
                print "No match!"
                exit()

#-*- coding:utf-8 -*-
# AUTHOR:   yaolili
# FILE:     vf.py
# ROLE:     TODO (some explanation)
# CREATED:  2015-11-28 20:55:11
# MODIFIED: 2015-11-30 20:10:39

import sys
import os
from graph import GraphSet
from map import Map

class Vf:
    __origin = None
    __sub = None
     
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
                    print "yes"
            elif v2 != index:
                
                if v2 not in (neighborVertexSet and mapGraph):
                    print "yes"
            else:
                print ""

    #meet feasibility rules or not, return true or false
    def isMeetRules(n, m, result, graphVertexSet, graphEdgeSet, subGraphVertexSet, subGraphEdgeSet):
        #label match failure 
        if(subGraphVertexSet[n] != graphVertexSet[m]):
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
    def dfsMatch(i, j, result):    
        
        curMap = Map(result)
        if curMap.isCovered(global sub.vertexSet[i]):
            return result
        
        subNeighbor = curMap.neighbor(i, global sub, 0)
        gNeighbor = curMap.neighbor(j, global origin, 1)   
       
        #mapSubGraph doesn't corver subGraphVertexSet, so subGraphNeighbor and graphNeighbor can't be empty 
        if not (subNeighbor and gNeighbor):
            print "in dfsMatch(), subNeighbor or gNeighbor is empty!"
            exit()
        
        #notice, choose one vertex in subGraphNeighbor is ok
        while(len(subNeighbor) > 1):
            subNeighbor.pop()

        #test usage!
        print "in dfsMatch() curMap: ", curMap
        print "in dfsMatch() subNeighbor: ", subNeighbor
        print "in dfsMatch() gNeighbor: ", gNeighbor
        print "in dfsMatch() result: ", result

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
        
    def main(f1, f2):

        global origin = GraphSet(f1)
        global sub = GraphSet(f2)
        for i in range(len(sub.graphSet)):     
            for j in range(len(origin.graphSet)):
                result = {}        
                result = dfsMatch(i, j, result)
                
                '''
                #remain to fix
                if len(result) == len(currentSubGraph):
                    print "Match! %s %d-th graph isomorphism %s %d-th graph! " %(f2, i, f1, j)
                    print result
                    exit()
                else:
                    print "No match!"
                    exit()
                '''    

        
    
    
   

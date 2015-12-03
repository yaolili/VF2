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
    def candidate(self, subNeighbor, gNeighbor):
        if not (subNeighbor and gNeighbor):
            print "Class Vf candidate() arguments value error! subNeighbor or gNeighbor is empty!"
            exit()
        if not isinstance(subNeighbor, list) and isinstance(gNeighbor, list):
            print "Class Vf candidate() arguments type error! type list expected!"
            exit()
        if not all(isinstance(x, int) for x in subNeighbor):
            print "Class Vf candidate() arguments type error! int in subNeighbor list expected!"
        if not all(isinstance(x, int) for x in gNeighbor):
            print "Class Vf candidate() arguments type error! int in gNeighbor list expected!"        
        
        pairs = []
        for i in range(len(subNeighbor)):
            for j in range(len(gNeighbor)):
                string = str(subNeighbor[i]) + ":" + str(gNeighbor[j])
                pairs.append(string)
        return pairs

    #type = 0, pre; type = 1, succ    
    def preSucc(self, vertexNeighbor, map, type):
        #vertexNeighbor can be empty
        if not map:
            print "Class Vf preSucc() arguments value error! map is empty!"
            exit()
        if not (isinstance(vertexNeighbor, list) and isinstance(map, list)):
            print "Class Vf preSucc() arguments type error! vertexNeighbor and map expected list!"
            exit()
        if not (type == 0 or type == 1):
            print "Class Vf preSucc() arguments value error! type expected 0 or 1!"
           
        result = []
        #succ
        if type:
            for vertex in vertexNeighbor:
                if vertex not in map:                   
                    result.append(vertex)
        #pre
        else:
            for vertex in vertexNeighbor:
                if vertex in map:
                    result.append(vertex)
        return result

    #meet feasibility rules or not, return true or false
    def isMeetRules(self, pairIndex, result):
        #remain to check arguments
        
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
    def dfsMatch(self, i, j, result):    
        #remain to check arguments
        curMap = Map(result)
        if curMap.isCovered(self.__sub.curVSet(i)):
            return result
        
        subNeighbor = curMap.neighbor(i, self.__sub, 0)
        gNeighbor = curMap.neighbor(j, self.__origin, 1)   
       
        #mapSubGraph doesn't corver subGraphVertexSet, so subGraphNeighbor and graphNeighbor can't be empty 
        if not (subNeighbor and gNeighbor):
            print "Class Vf dfsMatch(), subNeighbor or gNeighbor is empty!"
            exit()
        
        #notice, choose one vertex in subGraphNeighbor is ok
        while(len(subNeighbor) > 1):
            print "Class Vf dfsMatch() subNeighbor: ", subNeighbor
            subNeighbor.pop()

        #test usage!
        print "Class Vf dfsMatch() curMap.subMap(): ", curMap.subMap()
        print "Class Vf dfsMatch() curMap.gMap(): ", curMap.gMap()
        print "Class Vf dfsMatch() subNeighbor: ", subNeighbor
        print "Class Vf dfsMatch() gNeighbor: ", gNeighbor
        print "Class Vf dfsMatch() result: ", result

        pairs = self.candidate(subNeighbor, gNeighbor)
        print "Class Vf dfsMatch() pairs: ", pairs
        if not pairs:
            return result
                
        for key in pairs:
            v1, v2 = key.strip().split(":")
            #remain to fix
            if(isMeetRules(v1, v2, result, graphVertexSet, graphEdgeSet, subGraphVertexSet, subGraphEdgeSet)):
                
                result[v1] = v2
                
                dfsMatch(currentSubGraph, currentGraph, result)       
                
                result.pop(key)
        return result
        
    def main(self, f1, f2, f3):
        #remain to check arguments
        self.__origin = GraphSet(f1)
        self.__sub = GraphSet(f2)
        
        out = file(f3, "w+")
        subLen = len(self.__sub.graphSet())
        gLen = len(self.__origin.graphSet())
        
        for i in range(subLen):          
            for j in range(gLen):
                result = {}        
                result = self.dfsMatch(i, j, result)                                               
                if len(result) == len(self.__sub.curVSet(i)):
                    out.write("Match! " + f2 + " " + str(i) + "-th graph isomorphism " + f1 + " " + str(j) + "-th graph!\n")
                    out.write(str(result) + "\n\n")   
        out.close()
        
    
    
   

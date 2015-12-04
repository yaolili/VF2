#-*- coding:utf-8 -*-
# AUTHOR:   yaolili
# FILE:     map.py
# ROLE:     current map result
# CREATED:  2015-11-28 20:55:11
# MODIFIED: 2015-12-04 16:01:43

from itertools import chain
from graph import GraphSet

class Map:   
    
    def __init__(self, result):  
        self.__subMap = []
        self.__gMap = []    
        if type(result) is not dict:
            print "Class Map __init__() argument type error! dict expected!"
            exit()
        if result:             
            for key in result:     
                self.__subMap.append(key)
                self.__gMap.append(result[key])
                
    def subMap(self):
        return self.__subMap
        
    def gMap(self):
        return self.__gMap
    
    
    #notice, here is subVertexSet
    def isCovered(self, vertexSet):
        print "Class Map isCovered() len(self.__subMap): ", len(self.__subMap)
        print "Class Map isCovered() len(vertexSet): ", len(vertexSet)
        if len(self.__subMap) == len(vertexSet):
            return True
        else:
            return False
            
    #type = 0, subGraph; type = 1, graph
    def neighbor(self, offset, graph, type, isInMap):
        if not isinstance(graph, GraphSet):
            print "Class Map neighbor() argument type error!"
            exit()
        if not (type == 1 or type == 0):
            print "Class Map neighbor() argument value error! type expected 0 or 1!"
            exit()
        if not (isInMap == True or isInMap == False):
			print "Class Map neighbor() argument value error! isInMap expected True or False!"
			exit()
            
        VESet = graph.curVESet(offset)  
        
        neighbor = []
        if type:
            curMap = self.__gMap
        else:
            curMap = self.__subMap
            
        #print "Class Map neighbor() VESet: ", VESet
        #print "Class Map neighbor() curMap: ", curMap
        for index in curMap:
            aList = VESet[index]
            #print "Class Map neighbor() aList: ", aList
            for i in range(len(aList)):
                v1, v2 = aList[i].strip().split(":")
                if int(v1) != index:
					v = int(v1)													
                elif int(v2) != index:
					v = int(v2)
                else:
                    print "Class Map subNeighbor() VESet error!"
                    exit()
                
                if isInMap and (v not in neighbor):
				    neighbor.append(v)
                elif v not in chain(neighbor, curMap):
					neighbor.append(v)			
                else:
                    continue

        if not neighbor:
            for index in graph.curVSet(offset):
                if index not in curMap:
                    neighbor.append(int(index))               
        return neighbor
    
    
   

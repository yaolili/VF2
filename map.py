#-*- coding:utf-8 -*-
# AUTHOR:   yaolili
# FILE:     map.py
# ROLE:     current map result
# CREATED:  2015-11-28 20:55:11
# MODIFIED: 2015-11-30 20:10:39

from graph import GraphSet

class Map:

    __subMap = []
    __gMap = []
    
    def __init__(self, result):     
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
        if len(self.__subMap) == len(vertexSet):
            return True
        else:
            return False
            
    #type = 0, subGraph; type = 1, graph
    def neighbor(self, offset, graph, type):
        if not isinstance(graph, GraphSet):
            print "Class Map neighbor() argument type error!"
            exit()
        if not (type == 1 or type == 0):
            print "Class Map neighbor() argument value error! type expected 0 or 1!"
            exit()
            
        VESet = graph.curVESet(offset)        
        neighbor = []
        if type:
            curMap = self.__gMap
        else:
            curMap = self.__subMap
        
        #print "curMap: ", curMap
        for index in curMap:
            aList = VESet[index]
            #print "aList: ", aList
            for i in range(len(aList)):
                v1, v2 = aList[i].strip.split(":")
                if int(v1) != index:
                    if int(v1) not in neighbor:
                        neighbor.append(int(v1))
                elif int(v2) != index:
                    if int(v2) not in neighbor:
                        neighbor.append(int(v2))
                else:
                    print "Class Map subNeighbor() VESet error!"
                    exit()
        if not neighbor:
            for index in graph.curVSet(offset):
                if index not in curMap:
                    neighbor.append(int(index))               
        return neighbor
    
    
   
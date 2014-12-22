# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

# script for Floyd Warshall Algorithm- All Pair Shortest Path
INF = 999999999
def printSolution(distGraph):
    string = "inf"
    nodes = distGraph.keys()
    for n in nodes:
        print "%10s" % (n),
    print "  "
    for i in nodes:
        print"%s" % (i),
        for j in nodes:
            if distGraph[i][j] == INF:
                print "%10s" % (string),
            else:
                print "%10s" % (distGraph[i][j]),
        print" "
def floydWarshall(graph):
    nodes = graph.keys()
    distance = {}
    for n in nodes:
        distance[n] = {}
        for k in nodes:
            distance[n][k] = graph[n][k]
    for k in nodes:
        for i in nodes:
            for j in nodes:
                if distance[i][k] + distance[k][j] < distance[i][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
    printSolution(distance)
if __name__ == '__main__':
    graph = {'A':{'A':0, 'B':6, 'C':INF, 'D':6, 'E':7},
             'B':{'A':INF, 'B':0, 'C':5, 'D':INF, 'E':INF},
             'C':{'A':INF, 'B':INF, 'C':0, 'D':9, 'E':3},
             'D':{'A':INF, 'B':INF, 'C':9, 'D':0, 'E':7},
             'E':{'A':INF, 'B':4, 'C':INF, 'D':INF, 'E':0}
             }
    floydWarshall(graph)

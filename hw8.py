'''
Created on Apr 1, 2019

@author: lindsaymagg
'''
import itertools
import math

############### HELPER FUNCTIONS #################

def findCycle(M):
    """
    This function returns a cycle (represented by a list of vertices) containing a given
        vertex v using only vertices in list 'path' and reachable vertices not yet in 'visited'
        if such a cycle exists, otherwise it returns None.

    Input:
        M, list[list[int]]: a symmetric matrix representing an undirected connected graph
            where M[i][j] is None if there is no edge between vertex i and vertex j, otherwise
            it is the weight of the edge between them. Again, the graph represented by M is assumed
            to be connected!     

    Output:
        C, list[int]: a list of distinct vertices (ints) for which any two consecutive vertices
            are adjacent according to M, as well as the first and last vertices in C.
    """

    assert isSymmetric(M), "input graph not symmetric"
    assert isConnected(M), "input graph not connected"

    n = len(M)
    visited = set()
    path = []
    
    for v in range(n):

        if v not in visited:

            cycle = findCycleFrom(v, M, path, visited)

            if cycle is not None:
                return cycle

    return cycle

def isSymmetric(M):
    """
    This function returns True if the matrix M is symmetric (and square), and False otherwise.
    """

    n = len(M)
    if list(map(len,M)) != [n]*n:
        # if M is not square
        return False

    return all(all(M[i][j] == M[j][i] for j in range(i+1,n)) for i in range(n))

def isConnected(M):
    """
    This function returns True if the graph represented by M is connected, and False otherwise.
    """

    n = len(M)
    visited = set()
    path = []

    findCycleFrom(0, M, path, visited)
    return len(visited) == n

def createExampleGraph():
    """
    This function returns the matrix found on the handout for testing purposes.
    """
    M = [
        [None, 2, -5, 3, 4],
        [2, None, None, -8, 9],
        [-5, None, None, 5, None],
        [3, -8, 5, None, -7],
        [4, 9, None, -7, None],
    ]
    return M

def findCycleFrom(v, M, path, visited):
    """
    NOTE: This function is NOT to be called directly and intended for use by isConnected(M) and
        findCycle(M). It is essentially a recursive implementation of DFS.

    This function returns a cycle (represented by a list of vertices) containing a given
        vertex v using only vertices in list 'path' and reachable vertices not yet in 'visited'
        if such a cycle exists, otherwise it returns None.

    Input:
        v, int: an integer between 0 and len(M) representing vertex v.
        M, list[list[int]]: a symmetric matrix representing an undirected connected graph
            where M[i][j] is None if there is no edge between vertex i and vertex j, otherwise
            it is the weight of the edge between them. Again, the graph represented by M is assumed
            to be connected!
        path, list[int]: the list of vertices visited in order by DFS to the input vertex v.
        visited, set[int]: a set of vertices visited by DFS.

    Output:
        C, list[int]: a list of distinct vertices (ints) for which any two consecutive vertices
            are adjacent according to M, as well as the first and last vertices in C.
    """

    assert v not in path, "called on vertex already in path"
    assert v not in visited, "called on vertex already visited"

    visited.add(v)
    path.append(v)

    cycle = None
    for u in neighbors(v,M):
        
        if u in path and path[-2] != u: # if on path and not immediately before v (path[-1])
            assert u in visited, "found vertex in path that is not visited"

            # u is preceding v in the path, and just found edge (v,u), 
            #   so the subpath from u to v with (v,u) makes a cycle.
            
            i = path.index(u)
            cycle = path[i:]

        elif u in visited: # and not in path
            continue

        else: # u not visited
            new_cycle = findCycleFrom(u, M, path, visited)
            
            if new_cycle is not None:
                cycle = new_cycle

    assert path[-1] == v, "last vertex in path different than current vertex"
    path.pop()

    return cycle

def neighbors(u,M):
    """
    NOTE: This function is NOT to be called directly and intended for use by isConnected(M) and
        findCycle(M).

    This function returns the vertices adjacent to vertex u in the graph
        represented by M.
    """
    return [v for v,w in enumerate(M[u]) if w is not None]

################ INCOMPLETE FUNCTIONS #################

def findMST(M):
    """
    This function returns the total weight of the minimum spanning tree (MST) of the undirected connected graph G
    represented by the input matrix M using the specific algorithm as follows:

        While the graph G contains a cycle:
            1) find a cycle in G, then
            2) delete the heaviest edge in the cycle from G.

    To do so, you can use the function "findCycle(M)" given above. You might find the given functions isConnected(M)
    and isSymmetric(M) useful when testing your implementation.

    Input:
        M, list[list[int]]: a symmetric matrix representing an undirected connected graph
            where M[i][j] is None if there is no edge between vertex i and vertex j, otherwise
            it is the weight of the edge between them. Again, the graph represented by M is assumed
            to be connected!

    Output:
        T: list[list[int]]: a symmetric matrix representing an MST of the input graph M.

    Example:
        See the handout for example code and a figure.
    """
    matrix = M
    while (True):
        cycle = findCycle(M)
        if (cycle == None):
            # if no cycles, return MST
            return matrix
        else:
            # remove heaviest edge of cycle
            # for every two vertices, make list
            listy = []
            print("cycle is ")
            print(cycle)
            for v in range(len(cycle)):
                # get list of vertices and edge weights
                smolList = []
                if (cycle[v] != cycle[-1]):
                    smolList.append(cycle[v])
                    smolList.append(cycle[v+1])
                    smolList.append(M[cycle[v]][cycle[v+1]])
                    print("smolList is ")
                    print(smolList)
                listy.append(smolList)
            smolList.append(cycle[0])
            smolList.append(cycle[-1])
            smolList.append(M[cycle[0]][cycle[-1]])
            print("smolList is ")
            print(smolList)
            print("listy is ")
            print(listy)
            maxEdgeWeight = -math.inf
            maxIndex = 0
            counter = 0
            for item in listy:
                print("item is ")
                print(item)
                if (item[2] > maxEdgeWeight):
                    print(item[2])
                    print("is greater than ")
                    print(maxEdgeWeight)
                    maxIndex = counter
                    maxEdgeWeight = item[2]
                    print("maxEdge is now ")
                    print(maxEdgeWeight)
                    print("counter ")
                    print(counter)
                counter += 1
            edgy = listy[maxIndex]
            print("time to remove ")
            print(edgy)
            x = edgy[0]
            y = edgy[1]
            matrix[x][y] = None
            matrix[y][x] = None
            print(matrix)
    return matrix
            

if __name__ == '__main__':
    # Write your testing code below this line
    # and INSIDE this if-block! Feel free to
    # delete this and the given test code.

    X = createExampleGraph()
    print("Matrix of graph:")
    for x in X:
        print(x)

    print()

    T = findMST(X)
    
    print()
    print("MST of graph:")
    
    print()
    for t in T:
        print(t)
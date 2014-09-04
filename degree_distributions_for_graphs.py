'''
Project 1 - Degree distributions for graphs
'''
EX_GRAPH0 = {0:set([1, 2]), 1:set([]), 2:set([])}
EX_GRAPH1 = {0:set([1, 4, 5]), 1:set([2, 6]), 2:set([3]), 3:set([0]), 4:set([1]), 5:set([2]), 6:set([])}
EX_GRAPH2 = {0:set([1, 4, 5]), 1:set([2, 6]), 2:set([3, 7]), 3:set([7]), 4:set([1]), 5:set([2]), 6:set([]), 7:set([3]), 8:set([1, 2]), 9:set([0, 3, 4, 5, 6, 7])}
    
def make_complete_graph(num_nodes):
    '''
    Takes the number of nodes num_nodes and returns a dictionary corresponding to a complete directed graph with the specified number of nodes. 
    '''
    if num_nodes <= 1:
        return {0:set([])}
    graph = {}
    for num in range(num_nodes):
        all_num = range(num_nodes)
        all_num.remove(num)
        graph[num] = set(all_num)
    return graph

def compute_in_degrees(digraph):
    '''
    Takes a directed graph digraph (represented as a dictionary) and computes the in-degrees for the nodes in the graph. 
    '''
    in_degrees = {}
    for node in digraph.keys():
        in_degrees[node] = 0
        for edge_list in digraph.values():
            if node in edge_list:
                in_degrees[node] += 1
    return in_degrees

def in_degree_distribution(digraph):
    '''
    Takes a directed graph digraph (represented as a dictionary) and computes the unnormalized distribution of the in-degrees of the graph. 
    '''
    in_degrees = compute_in_degrees(digraph)
    in_degree_dis = dict.fromkeys(in_degrees.values(), 0)
    for in_degree in in_degrees.values():
        in_degree_dis[in_degree] += 1 
        #cnt = len(in_degrees[node])
        #if cnt != 0:
        #    in_degree_dis[node] = cnt
    return in_degree_dis

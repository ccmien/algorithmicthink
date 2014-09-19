"""
Connected components and graph resilience
"""
from collections import deque

def bfs_visited(ugraph, start_node):
    """
    Takes the undirected graph ugraph and the node start_node and returns the set consisting of all nodes that are visited by a breadth-first search that starts at start_node.
    """
    queue = deque()
    visited = set([start_node])
    queue.append(start_node)
    while len(queue) != 0:
        j_node = queue.popleft()
        for neighbor in ugraph[j_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return visited

def cc_visited(ugraph):
    """
    Takes the undirected graph ugraph and returns a list of sets, where each set consists of all the nodes (and nothing else) in a connected component, and there is exactly one set in the list for each connected component in ugraph and nothing else.
    """
    remaining_nodes = ugraph.keys()
    connected_component = []
    while len(remaining_nodes) != 0:
        any_node = remaining_nodes[0]
        any_node_visited = bfs_visited(ugraph, any_node)
        connected_component.append(any_node_visited)
        remaining_nodes = list(set(remaining_nodes).difference(set(any_node_visited)))
    return connected_component

def largest_cc_size(ugraph):
    """
    Takes the undirected graph ugraph and returns the size (an integer) of the largest connected component in ugraph.
    """
    if len(ugraph) == 0:
        return 0
    connected_component = cc_visited(ugraph)
    return max([len(x) for x in connected_component])

def compute_resilience(ugraph, attack_order):
    """
    Takes the undirected graph ugraph, a list of nodes attack_order and iterates through the nodes in attack_order. 
    """
    size_list = [largest_cc_size(ugraph)]
    for attack_node in attack_order:
        ugraph_update = {}
        for (vkey, vvalue) in ugraph.iteritems():           
            if vkey != attack_node:
                ugraph_update[vkey] = vvalue - set([attack_node])
        ugraph = ugraph_update
        size_list.append(largest_cc_size(ugraph))
    return size_list

'''
EX_GRAPH0 = {0:set([1, 2]), 1:set([]), 2:set([])}
EX_GRAPH1 = {0:set([1, 4, 5]), 1:set([2, 6]), 2:set([3]), 3:set([0]), 4:set([1]), 5:set([2]), 6:set([])} 
EX_GRAPH2 = {0:set([1, 4, 5]), 1:set([2, 6]), 2:set([3, 7]), 3:set([7]), 4:set([1]), 5:set([2]), 6:set([]), 7:set([3]), 8:set([1, 2]), 9:set([0, 3, 4, 5, 6, 7])}

print bfs_visited(EX_GRAPH0, 1)
print bfs_visited(EX_GRAPH0, 0)
print bfs_visited(EX_GRAPH0, 2)
print cc_visited(EX_GRAPH0)
print cc_visited(EX_GRAPH1)
print cc_visited(EX_GRAPH2)
print largest_cc_size(EX_GRAPH0)
print largest_cc_size(EX_GRAPH1)
print largest_cc_size(EX_GRAPH2)
print compute_resilience(EX_GRAPH0, [0])
print compute_resilience(EX_GRAPH1, [1, 2])
print compute_resilience(EX_GRAPH2, [1, 2])
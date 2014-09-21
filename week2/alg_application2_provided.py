"""
Provided code for Application portion of Module 2
"""

# general imports
import urllib2
import random
import time
import math

# CodeSkulptor import
#import simpleplot
#import codeskulptor
#codeskulptor.set_timeout(60)

# Desktop imports
import matplotlib.pyplot as plt


############################################
# Provided code

def copy_graph(graph):
    """
    Make a copy of a graph
    """
    new_graph = {}
    for node in graph:
        new_graph[node] = set(graph[node])
    return new_graph

def delete_node(ugraph, node):
    """
    Delete a node from an undirected graph
    """
    neighbors = ugraph[node]
    ugraph.pop(node)
    for neighbor in neighbors:
        ugraph[neighbor].remove(node)
    
def targeted_order(ugraph):
    """
    Compute a targeted attack order consisting
    of nodes of maximal degree
    
    Returns:
    A list of nodes
    """
    # copy the graph
    new_graph = copy_graph(ugraph)
    
    order = []    
    while len(new_graph) > 0:
        max_degree = -1
        for node in new_graph:
            if len(new_graph[node]) > max_degree:
                max_degree = len(new_graph[node])
                max_degree_node = node
        
        neighbors = new_graph[max_degree_node]
        new_graph.pop(max_degree_node)
        for neighbor in neighbors:
            new_graph[neighbor].remove(max_degree_node)

        order.append(max_degree_node)
    return order
    
def fast_targeted_order(ugraph):
    """
    Compute a fast targeted attack order consisting
    of nodes of maximal degree
    
    Returns:
    A list of nodes
    """
    n = len(ugraph)
    new_graph = copy_graph(ugraph)
    degree_sets = {}
    for node, neighbors in ugraph.iteritems():
        degree_sets.setdefault(len(neighbors), set()).add(node)
    order = []
    i = 0
    for k in range(n-1, 0, -1):
        if degree_sets.has_key(k):
            while len(degree_sets[k]) != 0:
                max_degree_node = degree_sets[k].pop()
                for neighbor in new_graph[max_degree_node]:
                    d = len(new_graph[neighbor])
                    degree_sets[d].remove(neighbor)
                    degree_sets.setdefault(d-1, set()).add(neighbor)                    
                order.append(max_degree_node)
                delete_node(new_graph, max_degree_node)
                i += 1
    if i < n:
        order.extend(new_graph.keys())
    return order    

##########################################################
# Code for loading computer network graph

NETWORK_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_rf7.txt"


def load_graph(graph_loc):
    """
    Function that loads a graph given the location 
    for a text representation of the graph
    
    Returns a dictionary that models a graph
    """
    graph_file = open(graph_loc)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ : -1]
    
    print "Loaded graph with", len(graph_lines), "nodes"
    
    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph

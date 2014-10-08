"""
Example code for creating and visualizing
cluster of county-based cancer risk data

Note that you must download the file
http://www.codeskulptor.org/#alg_clusters_matplotlib.py
to use the matplotlib version of this code
"""

# Flavor of Python - desktop or CodeSkulptor
DESKTOP = True

import math
import random
import urllib2
import alg_cluster
import alg_app3
import matplotlib.pyplot as plt

# conditional imports
if DESKTOP:
    import alg_project3      # desktop project solution
    import alg_clusters_matplotlib
else:
    #import userXX_XXXXXXXX as alg_project3_solution   # CodeSkulptor project solution
    import alg_clusters_simplegui
    import codeskulptor
    codeskulptor.set_timeout(30)


###################################################
# Code to load data tables

# URLs for cancer risk data tables of various sizes
# Numbers indicate number of counties in data table

DIRECTORY = "/Users/chenchaomin/GitHub/algorithmicthink/week3/data" 
DATA_3108_URL = DIRECTORY + "/unifiedCancerData_3108.csv"
DATA_896_URL = DIRECTORY + "/unifiedCancerData_896.csv"
DATA_290_URL = DIRECTORY + "/unifiedCancerData_290.csv"
DATA_111_URL = DIRECTORY + "/unifiedCancerData_111.csv"


def load_data_table(data_url):
    """
    Import a table of county-based cancer risk data
    from a csv format file
    """
    data_file = open(data_url)
    data = data_file.read()
    data_lines = data.split('\n')
    print "Loaded", len(data_lines), "data points"
    data_tokens = [line.split(',') for line in data_lines]
    return [[tokens[0], float(tokens[1]), float(tokens[2]), int(tokens[3]), float(tokens[4])] 
            for tokens in data_tokens]


############################################################
# Code to create sequential clustering
# Create alphabetical clusters for county data

def sequential_clustering(singleton_list, num_clusters):
    """
    Take a data table and create a list of clusters
    by partitioning the table into clusters based on its ordering
    
    Note that method may return num_clusters or num_clusters + 1 final clusters
    """
    
    cluster_list = []
    cluster_idx = 0
    total_clusters = len(singleton_list)
    cluster_size = float(total_clusters)  / num_clusters
    
    for cluster_idx in range(len(singleton_list)):
        new_cluster = singleton_list[cluster_idx]
        if math.floor(cluster_idx / cluster_size) != \
           math.floor((cluster_idx - 1) / cluster_size):
            cluster_list.append(new_cluster)
        else:
            cluster_list[-1] = cluster_list[-1].merge_clusters(new_cluster)
            
    return cluster_list
                

#####################################################################
# Code to load cancer data, compute a clustering and 
# visualize the results


def run_example():
    """
    Load a data table, compute a list of clusters and 
    plot a list of clusters

    Set DESKTOP = True/False to use either matplotlib or simplegui
    """
    data_table = load_data_table(DATA_896_URL)
    
    singleton_list = []
    for line in data_table:
        singleton_list.append(alg_cluster.Cluster(set([line[0]]), line[1], line[2], line[3], line[4]))
        
    #cluster_list = sequential_clustering(singleton_list, 15)	
    #print "Displaying", len(cluster_list), "sequential clusters"
    k_dis = []
    h_dis = []
    for cluster_num in xrange(6, 21):
        cluster_list = alg_project3.hierarchical_clustering([c.copy() for c in singleton_list], cluster_num)
        print "Displaying", len(cluster_list), "hierarchical clusters"
        h_dis.append(alg_app3.compute_distortion(cluster_list, data_table))

        cluster_list = alg_project3.kmeans_clustering([c.copy() for c in singleton_list], cluster_num, 5)	
        print "Displaying", len(cluster_list), "k-means clusters"
        k_dis.append(alg_app3.compute_distortion(cluster_list, data_table))

    xvals = range(6, 21)
    plt.plot(xvals, k_dis, '-b', label='kmeans_clustering (5 iteration)')
    plt.plot(xvals, h_dis, '-r', label='hierarchical_clustering')
    plt.legend(loc='upper right')
    plt.xlabel("number of clusters")
    plt.ylabel("distortion")
    plt.title("Distortion of 2 clustering methods: 896 counties")
    plt.show()
            
    # draw the clusters using matplotlib or simplegui
    """
    if DESKTOP:
        alg_clusters_matplotlib.plot_clusters(data_table, cluster_list, True)
    else:
        alg_clusters_simplegui.PlotClusters(data_table, cluster_list)
    """
run_example()

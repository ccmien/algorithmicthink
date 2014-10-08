"""
Project 3
Student will implement four functions:

slow_closest_pairs(cluster_list)
fast_closest_pair(cluster_list) - implement fast_helper()
hierarchical_clustering(cluster_list, num_clusters)
kmeans_clustering(cluster_list, num_clusters, num_iterations)

where cluster_list is a list of clusters in the plane
"""

import math
import alg_cluster



def pair_distance(cluster_list, idx1, idx2):
    """
    Helper function to compute Euclidean distance between two clusters
    in cluster_list with indices idx1 and idx2
    
    Returns tuple (dist, idx1, idx2) with idx1 < idx2 where dist is distance between
    cluster_list[idx1] and cluster_list[idx2]
    """
    return (cluster_list[idx1].distance(cluster_list[idx2]), min(idx1, idx2), max(idx1, idx2))


def slow_closest_pairs(cluster_list):
    """
    Compute the set of closest pairs of cluster in list of clusters
    using O(n^2) all pairs algorithm
    
    Returns the set of all tuples of the form (dist, idx1, idx2) 
    where the cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.   
    
    """
    dist = 999999
    closest_pairs = set([])
    for cls_idx, cluster in enumerate(cluster_list):
        for ocls_idx, other_cluster in enumerate(cluster_list):
            if cls_idx < ocls_idx:
                dist2 = cluster.distance(other_cluster)
                if dist2 < dist:
                    dist = dist2
                    closest_pairs = set([(dist2, cls_idx, ocls_idx)])
                elif dist2 == dist:
                    closest_pairs.add((dist2, cls_idx, ocls_idx))
    return closest_pairs 
                    
def fast_closest_pair(cluster_list):
    """
    Compute a closest pair of clusters in cluster_list
    using O(n log(n)) divide and conquer algorithm
    
    Returns a tuple (distance, idx1, idx2) with idx1 < idx 2 where
    cluster_list[idx1] and cluster_list[idx2]
    have the smallest distance dist of any pair of clusters
    """
        
    def fast_helper(cluster_list, horiz_order, vert_order):
        """
        Divide and conquer method for computing distance between closest pair of points
        Running time is O(n * log(n))
        
        horiz_order and vert_order are lists of indices for clusters
        ordered horizontally and vertically
        
        Returns a tuple (distance, idx1, idx2) with idx1 < idx 2 where
        cluster_list[idx1] and cluster_list[idx2]
        have the smallest distance dist of any pair of clusters
    
        """
        # base case
        num_point = len(horiz_order)
        if num_point <= 3:
            result = slow_closest_pairs([cluster_list[idx] for idx in horiz_order]).pop()
            return result[0], horiz_order[result[1]], horiz_order[result[2]]

        # divide
        mid_point = num_point/2
        horiz_l = horiz_order[:mid_point]
        horiz_r = horiz_order[mid_point:]
        vert_l = []
        vert_r = []
        for vert_idx in vert_order:
            if vert_idx in set(horiz_l):
                vert_l.append(vert_idx)
            else:
                vert_r.append(vert_idx)

        dist_l, idx1_l, idx2_l = fast_helper(cluster_list, horiz_l, vert_l)
        dist_r, idx1_r, idx2_r = fast_helper(cluster_list, horiz_r, vert_r)

        if dist_l < dist_r:
            dist, idx1, idx2 = dist_l, idx1_l, idx2_l
        else:
            dist, idx1, idx2 = dist_r, idx1_r, idx2_r

        horiz_mid = (cluster_list[horiz_order[mid_point-1]].horiz_center() + 
                    cluster_list[horiz_order[mid_point]].horiz_center())/2

        # conquer
        vert_s = []
        for vert_index in vert_order:
            if abs(cluster_list[vert_index].horiz_center() - horiz_mid) <= dist:
                vert_s.append(vert_index)
        for idx_u in range(0, len(vert_s)-1):
            for idx_v in range(idx_u+1, min(idx_u+4, len(vert_s))):
                dist2 = cluster_list[vert_s[idx_u]].distance(cluster_list[vert_s[idx_v]])
                if dist2 < dist:
                    dist, idx1, idx2 = dist2, vert_s[idx_u], vert_s[idx_v]
                
        return (dist, idx1, idx2)
            
    # compute list of indices for the clusters ordered in the horizontal direction
    hcoord_and_index = [(cluster_list[idx].horiz_center(), idx) 
                        for idx in range(len(cluster_list))]    
    hcoord_and_index.sort()
    horiz_order = [hcoord_and_index[idx][1] for idx in range(len(hcoord_and_index))]
     
    # compute list of indices for the clusters ordered in vertical direction
    vcoord_and_index = [(cluster_list[idx].vert_center(), idx) 
                        for idx in range(len(cluster_list))]    
    vcoord_and_index.sort()
    vert_order = [vcoord_and_index[idx][1] for idx in range(len(vcoord_and_index))]

    # compute answer recursively
    answer = fast_helper(cluster_list, horiz_order, vert_order) 
    return (answer[0], min(answer[1:]), max(answer[1:]))

def hierarchical_clustering(cluster_list, num_clusters):
    """
    Compute a hierarchical clustering of a set of clusters
    Note: the function mutates cluster_list
    
    Input: List of clusters, number of clusters
    Output: List of clusters whose length is num_clusters
    """
    while len(cluster_list) > num_clusters:
        _dist, idx1, idx2 = fast_closest_pair(cluster_list)
        cluster_list[idx1].merge_clusters(cluster_list[idx2])
        del cluster_list[idx2]
    return cluster_list

def kmeans_clustering(cluster_list, num_clusters, num_iterations):
    """
    Compute the k-means clustering of a set of clusters
    
    Input: List of clusters, number of clusters, number of iterations
    Output: List of clusters whose length is num_clusters
    """
    
    # initialize k-means clusters to be initial clusters with largest populations
    kcluster = sorted(cluster_list, key = lambda x: x.total_population())[-num_clusters:]
    
    for __i in xrange(num_iterations):
        cluster_result = [alg_cluster.Cluster(set([]), 0, 0, 0, 0) for _i in range(num_clusters)]
        for idx, cluster in enumerate(cluster_list):
            tmp_list = [cluster.distance(center) for center in kcluster]
            cluster_result[tmp_list.index(min(tmp_list))].merge_clusters(cluster_list[idx])
        kcluster = [c.copy() for c in cluster_result] 

    return cluster_result 

import random
import timeit
import matplotlib.pyplot as plt
import alg_cluster
import alg_project3

def gen_random_clusters(num_clusters):
    """
    creates a list of clusters where each cluster in this list corresponds to one randomly generated point in the square with corners (+-1,+-1)
    """
    cluster_result = [alg_cluster.Cluster(set([]), random.uniform(-1, 1), random.uniform(-1, 1), 0, 0) for _i in range(num_clusters)]
    return cluster_result

def efficiency_plot():
    time_slow = []
    time_fast = []
    for num_clusters in xrange(2, 201):
        cluster_list = gen_random_clusters(num_clusters)
        
        start_time = timeit.default_timer()
        alg_project3.slow_closest_pairs(cluster_list)
        time_slow.append(timeit.default_timer() - start_time)
        
        start_time = timeit.default_timer()
        alg_project3.fast_closest_pair(cluster_list)
        time_fast.append(timeit.default_timer() - start_time)

    xvals = range(2, 201)
    plt.plot(xvals, time_slow, '-b', label='slow_closest_pairs')
    plt.plot(xvals, time_fast, '-r', label='fast_closest_pair')
    plt.legend(loc='upper left')
    plt.xlabel("number of clusters")
    plt.ylabel("running time of functions in seconds")
    plt.title("Running Time of 2 Closest Pairs Function on Desktop Python")
    plt.show()

def compute_distortion(cluster_list, data_table):
    distortion = 0
    for cluster in cluster_list:
        distortion += cluster.cluster_error(data_table)
    return distortion

if __name__ == "__main__":
    efficiency_plot()

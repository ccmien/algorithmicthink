import sys
sys.path.append("..")
import alg_application2_provided as app2_prv
import week1.degree_distributions_for_graphs as distri
import graph_uer
import alg_upa_trial as upa
import random
import BFS
import matplotlib.pyplot as plt
import time


def graph_upa(node_num, out_m):
    graph = distri.make_complete_graph(out_m)
    out_node = upa.UPATrial(out_m)

    for num in range(out_m, node_num):
        graph.setdefault(num, set()).update(out_node.run_trial(out_m))
        for neighbor in graph[num]:
        	graph.setdefault(neighbor, set()).add(num)
    return graph



def random_order(ugraph):
   return random.sample(ugraph.keys(), len(ugraph))

def q1_plot():
    # comp graph
    comp_graph = app2_prv.load_graph("alg_rf7.txt")
    comp_distri = distri.in_degree_distribution(comp_graph)
    comp_nodes = sum(comp_distri.values())
    comp_edges = sum([x * y for (x, y) in comp_distri.iteritems()])/2
    comp_prob = float(comp_edges)/comp_nodes/(comp_nodes-1)
    print "comp nodes", comp_nodes
    print "comp edges", comp_edges
    print "comp prob", comp_prob
    print "comp m", comp_edges/float(comp_nodes)

    # uer graph
    uer_graph = graph_uer.graph_uer(comp_nodes, comp_prob)
    uer_distri = distri.in_degree_distribution(uer_graph)
    uer_edges = sum([x * y for (x, y) in uer_distri.iteritems()])/2
    print "uer nodes", sum(uer_distri.values())
    print "uer edges", uer_edges

    # upa graph

    upa_graph = graph_upa(comp_nodes, 2)
    upa_distri = distri.in_degree_distribution(upa_graph)
    upa_edges = sum([x * y for (x, y) in upa_distri.iteritems()])/2
    print "upa nodes", sum(upa_distri.values())
    print "edges", upa_edges

    # resilience

    comp_resi = BFS.compute_resilience(comp_graph, random_order(comp_graph))
    upa_resi = BFS.compute_resilience(upa_graph, random_order(upa_graph))
    uer_resi = BFS.compute_resilience(uer_graph, random_order(uer_graph))
    print "compute_resilience completed"

    xvals = range(comp_nodes+1)
    plt.plot(xvals, comp_resi, '-b', label='computer network')
    plt.plot(xvals, upa_resi, '-r', label='UPA m = 2')
    plt.plot(xvals, uer_resi, '-g', label='ER p = 0.0017')
    plt.legend(loc='upper right')
    plt.xlabel("number of nodes removed")
    plt.ylabel("size of the largest connect component")
    plt.title("Resilience of 3 Types of Undirected Graphs")
    plt.show()
    
def q3_plot():
    running_time = []
    fast_running_time = []
    for n in range(10, 1000, 10):
        upa_graph = graph_upa(n, 5)
        time1 = time.time()
        tmp = app2_prv.targeted_order(upa_graph)
        running_time.append(time.time() - time1)
        fast_time1 = time.time()
        tmp2 = app2_prv.fast_targeted_order(upa_graph)
        fast_running_time.append(time.time() - fast_time1)
    xvals = range(10, 1000, 10)
    plt.plot(xvals, running_time, '-b', label='targeted_order')
    plt.plot(xvals, fast_running_time, '-r', label='fast_targeted_order')
    plt.legend(loc='upper left')
    plt.xlabel("number of nodes in UPA graph")
    plt.ylabel("running time (seconds)")
    plt.title("Targeted Order Algorithm Running Time Result on Desktop Python")
    plt.show()


def q4_plot():
    # comp graph
    comp_graph = app2_prv.load_graph("alg_rf7.txt")
    comp_distri = distri.in_degree_distribution(comp_graph)
    comp_nodes = sum(comp_distri.values())
    comp_edges = sum([x * y for (x, y) in comp_distri.iteritems()])/2
    comp_prob = float(comp_edges)/comp_nodes/(comp_nodes-1)
    print "comp nodes", comp_nodes
    print "comp edges", comp_edges
    print "comp prob", comp_prob
    print "comp m", comp_edges/float(comp_nodes)

    # uer graph
    uer_graph = graph_uer.graph_uer(comp_nodes, comp_prob)
    uer_distri = distri.in_degree_distribution(uer_graph)
    uer_edges = sum([x * y for (x, y) in uer_distri.iteritems()])/2
    print "uer nodes", sum(uer_distri.values())
    print "uer edges", uer_edges

    # upa graph

    upa_graph = graph_upa(comp_nodes, 2)
    upa_distri = distri.in_degree_distribution(upa_graph)
    upa_edges = sum([x * y for (x, y) in upa_distri.iteritems()])/2
    print "upa nodes", sum(upa_distri.values())
    print "edges", upa_edges

    # resilience

    comp_resi = BFS.compute_resilience(comp_graph, app2_prv.fast_targeted_order(comp_graph))
    upa_resi = BFS.compute_resilience(upa_graph, app2_prv.fast_targeted_order(upa_graph))
    uer_resi = BFS.compute_resilience(uer_graph, app2_prv.fast_targeted_order(uer_graph))
    print "compute_resilience completed"

    xvals = range(comp_nodes+1)
    plt.plot(xvals, comp_resi, '-b', label='computer network')
    plt.plot(xvals, upa_resi, '-r', label='UPA m = 2')
    plt.plot(xvals, uer_resi, '-g', label='ER p = 0.0017')
    plt.legend(loc='upper right')
    plt.xlabel("number of nodes removed")
    plt.ylabel("size of the largest connect component")
    plt.title("Resilience of 3 Types of Undirected Graphs(targeted order)")
    plt.show()

if __name__ == '__main__':
    q4_plot()

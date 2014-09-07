import degree_distributions_for_graphs as degree_dis
import alg_load_graph
import matplotlib.pyplot as plt

def plot_distri(digraph):
    """
    plot log/log distribution of digraph
    """
    distri = degree_dis.in_degree_distribution(digraph)
    sum_degree = float(sum(distri.values()))
    distriy = [x/sum_degree for x in distri.values()]
    distrix = distri.keys()
    plt.loglog(distrix, distriy, "bo")
    plt.xlabel("Cite Counts(log)")
    plt.ylabel("Indegree Frequency(log)")
    plt.title("Indegree Distribution for DPA Graph")
    plt.show()

if __name__ == "__main__":
    citation_graph = alg_load_graph.load_graph("http://temporary-files.qiniudn.com/alg_phys-cite-1.txt")
    plot_distri(citation_graph)

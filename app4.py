import alg_dpa_trial 
import degree_distributions_for_graphs as degree_dis

def graph_dpa(node_num, out_m):
    graph = degree_dis.make_complete_graph(out_m)
    out_node = alg_dpa_trial.DPATrial(out_m)

    for num in range(out_m, node_num):
        graph[num] = out_node.run_trial(out_m)
    return graph

    


import random

def graph_uer(node_num, prob):
    graph = {}
    for num in range(node_num):
        graph.setdefault(num, set())
        for other in range(node_num)[:num] + range(node_num)[(num+1):]:
            a = random.random()
            if a < prob:
                graph.setdefault(num, set()).add(other)
                graph.setdefault(other, set()).add(num)
    return graph

if __name__ == "__main__":
    print graph_uer(5, 0.5)
    print graph_uer(10, 0.5)

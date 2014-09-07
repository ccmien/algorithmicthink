import random

def graph_er(node_num, prob):
    graph = {}
    for num in range(node_num):
        graph[num] = set()
        for other in range(node_num)[:num] + range(node_num)[(num+1):]:
            a = random.random()
            if a < prob:
                graph[num].add(other)
    return graph

if __name__ == "__main__":
    print graph_er(5, 0.5)
    print graph_er(10, 0.5)

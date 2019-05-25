import numpy as np


def load_graphs():
    graphs = list()
    for i in range(2,10):
        f = open('graph_files/graph' + str(i) + 'c','r')
        graphs.append(list())
        contents = f.read()
        tab = contents.split('\n\n')
        for graph in tab:
            a = np.fromiter(''.join(graph.split('\n')[1:]),'int')
            a.shape = i,i
            graphs[i - 2].append(a)
        f.close()
    return graphs


def delta(graph):
    evalues, _ = np.linalg.eigh(graph)
    return evalues[len(evalues) - 1] - evalues[0]

def s(n, graphs):
    return max(list(map(delta, graphs[n-2])))



gr = load_graphs()

for i in range(2, 10):
    print(s(i,gr))

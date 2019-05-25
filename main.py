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

load_graphs()

import numpy as np

def load_graphs():
    graphs = list()
    for i in range(2,10):
        f = open('graph_files/graph' + str(i) + 'c','r')
        graphs.append(list())
        tab = f.read().split('\n\n')
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

def gamma(n, graphs):
    return list(filter(lambda x: abs(x[1]) < 1.0e-11, enumerate(list(map(lambda x: delta(x) - n, graphs[n - 2])), 1)))

def random_graph(N):
    b = np.random.randint(0, 1 + 20, size=(N, N))
    graph = (b + b.T)
    graph = graph.astype(bool)
    np.fill_diagonal(graph,0)
    graph = graph.astype(int)
    return graph

gr = load_graphs()

print('Wartości funkcji s oraz gamma:')#podpunkt 1
for i in range(2, 10):
    s_val = s(i,gr)
    print('n = ' + str(i) + ': ')
    print(s_val)
    print(s_val - i)

print('Wartości gamma bliskie zeru, oraz numery grafów:')#podpunkt 2
for i in range(2, 10):
    print(gamma(i, gr))


#list_graph = [random_graph(60) for _ in range(100)]# podpunkt 3
#list_delta = [delta(graph) - 60 for graph in list_graph]
#max_ind = np.argmax(list_delta)
#print(list_delta[max_ind])
#np.savetxt('graph.out',list_graph[max_ind],fmt='%d')


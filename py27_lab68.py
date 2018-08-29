import graphviz

import graphviz as gv
import itertools

g1 = gv.Digraph(format='svg')

nodeList = list('ABC')
for node in nodeList:
    g1.node(node)
#edges = itertools.combinations(nodeList, 2)
edges = itertools.permutations(nodeList, 2)
for n1, n2 in edges:
    g1.edge(n1, n2)

g1.render('.//graph//lab68')
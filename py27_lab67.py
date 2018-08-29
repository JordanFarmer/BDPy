# pip install graphviz
import graphviz as gv

g1 = gv.Graph(format='svg')
g1.node('A')
g1.node('B')
g1.node('C')
g1.edge('A', 'B')
g1.edge('A', 'C')
g1.edge('A', 'A')
g1.edge('C', 'C')
print g1.source
g1.render('.\\graph\\lab67')
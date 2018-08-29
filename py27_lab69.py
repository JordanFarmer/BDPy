# encoding=UTF-8
import graphviz as gv
import functools

graph = functools.partial(gv.Graph, format='svg')
digraph = functools.partial(gv.Digraph, format='svg')
g3 = graph()
g4 = digraph()


def add_nodes(graph, nodes):
    for n in nodes:
        if isinstance(n, tuple):
            graph.node(n[0], **n[1])
        else:
            graph.node(n)
    return graph


def add_edges(graph, edges):
    for e in edges:
        if isinstance(e[0], tuple):
            graph.edge(*e[0], **e[1])
        else:
            graph.edge(*e)
    return graph


nodes = ['A', 'B', 'C']
edges = [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B')]
g3 = add_nodes(g3, nodes)
g3 = add_edges(g3, edges=edges)
g3.render('.//graph//lab69_g3')

g4 = add_nodes(g4, nodes)
g4 = add_edges(g4, edges=edges)
g4.render('.//graph//lab69_g4')

completeNodes = [('A', {'label': 'NodeA'}),
                 ('B', {'label': 'Node...B'}),
                 ('C', {'label': u'中文'}),
                 ('D', {})]
completeEdges = [(('A', 'B'), {'label': 'Edge1'}), (('A', 'C'), {'label': 'Edge2'}),
                 (('B', 'C'), {'label': u'關聯'}), (('B', 'D'), {})]
g5 = digraph()
g5 = add_nodes(g5, completeNodes)
g5 = add_edges(g5, completeEdges)
g5.render('.//graph//lab69_g5')

styles = {
    'graph': {
        'label': u'示範圖檔',
        'fontsize': '24',
        'fontcolor': '#550000',
        'bgcolor': '#88FFFF',
        'rankdir': 'TB',
        'fillcolor': '88FF88'
    },
    'nodes': {
        'fontname': 'Consolas',
        'shape': 'box',
        'fontcolor': '#9999FF',
        'color': 'black',
        'style': 'filled',
        'fillColor': '#222200'
    },
    'edges': {
        'style': 'dotted',
        'color': '#004499',
        'arrowhead': 'open',
        'fontname': u'標楷體',
        'fontsize': '24',
        # 'fontcolor': '#22FF88'
    }
}


def apply_styles(graph, styles):
    graph.graph_attr.update(('graph' in styles and styles['graph']) or {})
    graph.node_attr.update(('nodes' in styles and styles['nodes']) or {})
    graph.edge_attr.update(('edges' in styles and styles['edges']) or {})
    return graph


g6 = apply_styles(g5, styles)
g6.render('.//graph//lab69_g6')
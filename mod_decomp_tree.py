import matplotlib.pyplot as plt
import networkx as nx
import pydot
from networkx.drawing.nx_pydot import graphviz_layout
import csv
from ast import literal_eval

def control(decomposed):

    graph = nx.DiGraph()

    def create_edges(decomposition):
        
        decomposition = list(decomposition)
        
        while graph.has_node(decomposition[0]):    
            decomposition[0] = decomposition[0] + '.'

        node = (decomposition[0])
        children = decomposition[1]
        graph.add_node(node)

        for child in children:
            if isinstance(child,int):
                graph.add_edge(node,child)
            else:
                parent = create_edges(child)
                graph.add_edge(node, parent)

        return node
    
    create_edges(decomposed)
    return graph

def display_tree(graph):
    colour_map = {}
    pos = graphviz_layout(graph, prog = "dot")
    for node in graph.nodes():
        if isinstance(node, str):
            colour_map[node] = 'pink'
        else:
            colour_map[node] = 'blue'
    colour_mapping = [colour_map[node] for node in graph.nodes()]

    nx.draw(graph, pos, with_labels = True, \
            edge_color='black', width=1, linewidths=1, \
            node_size=500, node_color=colour_mapping, alpha=0.9)
    plt.show()

decomposed = "('SERIES', [4, 1, ('PARALLEL', [0, 2, 3, 5, 6])])"
decomposed = literal_eval(decomposed)
print(decomposed)
out_tree = control(decomposed)
display_tree(out_tree)
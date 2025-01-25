import matplotlib.pyplot as plt
import networkx as nx
import pydot
from networkx.drawing.nx_pydot import graphviz_layout
from ast import literal_eval
import re
import os

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

def display_tree(graph, destination):
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
    # plt.show()
    plt.savefig(destination)
    plt.close()

def make_compatible(txt):
    txt = re.sub("SERIES", "'SERIES'", txt)
    txt = re.sub("PARALLEL", "'PARALLEL'", txt)
    txt = re.sub("PRIME", "'PRIME'", txt)

    return txt

# decomposed = "('SERIES', [4, 1, ('PARALLEL', [0, 2, 3, 5, 6])])"
# decomposed = literal_eval(decomposed)
# print(decomposed)
# out_tree = control(decomposed)
# display_tree(out_tree)

def main():
    home = "./html_files/order"
    for size in os.listdir(home):
        if size != '7':
            continue
        home1 = home + "/" + size
        for graph in os.listdir(home1):
            filepath = home1 + "/" + graph + "/modular_decomposition.txt"
            with open(filepath, 'rt') as f:
                txt = f.readline()
                txt = make_compatible(txt)
            txt = literal_eval(txt)
            out_tree = control(txt)
            destination = home1 + "/" + graph + "/modular_decomposition.png"
            display_tree(out_tree, destination)

if __name__=="__main__":
    main()
            
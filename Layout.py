import networkx as nx
import pydot
from networkx.drawing.nx_pydot import graphviz_layout
from tkinter import colorchooser

layout_options = ["Force-Directed (Fruchterman-Reingold)", "Hierarchical (Tree)",
                  "Hierarchical (Radial)", "Eigenvector", "Circular", "Shell", "Planar"]
draw_vars = {
        'pos': None,
        'with_labels': True,
        'node_size': 1000,
        'node_color': '#ff0000',
        'node_shape': 'o',
        'width': 1,
        'edge_color': '#0000ff',
        'arrows': True,
        'alpha': 1,
}


def choose_node_color():
    color_code = colorchooser.askcolor(title="Choose Nodes Color")
    if color_code[1]:  # Check if a color was chosen
        print('node_color: ', color_code[1])
        draw_vars['node_color'] = color_code[1]


def algorithm(G, selected_layout):
    print('selected_layout: ', selected_layout)
    layout_func = selected_layout
    pos = None

    if layout_func == "Force-Directed (Fruchterman-Reingold)":
        pos = nx.spring_layout(G)
    elif layout_func == "Hierarchical (Tree)":
        pos = graphviz_layout(G, prog='dot')
    elif layout_func == "Hierarchical (Radial)":
        pos = graphviz_layout(G, prog='twopi')
    elif layout_func == "Eigenvector":
        pos = nx.spectral_layout(G)
    elif layout_func == "Circular":
        pos = nx.circular_layout(G)
    elif layout_func == "Shell":
        pos = nx.shell_layout(G)
    elif layout_func == "Planar":
        pos = nx.planar_layout(G)

    draw_vars['pos'] = pos

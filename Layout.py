import networkx as nx
import pydot
from networkx.drawing.nx_pydot import graphviz_layout
from tkinter import colorchooser

layout_options = ["Force-Directed (Fruchterman-Reingold)", "Hierarchical (Tree)",
                  "Hierarchical (Radial)", "Eigenvector", "Circular", "Shell", "Planar"]
draw_vars = {
    'pos': None,
    'with_labels': True,
    'node_size': 500,
    'node_color': '#cfecf7',
    'node_shape': 'o',
    'width': 1,
    'edge_color': '#000000',
    'arrows': True,
}
attribute_to_show = None


def choose_node_color():
    print()
    color_code = colorchooser.askcolor(title="Choose Nodes Color")
    if color_code[1]:  # Check if a color was chosen
        print('node_color: ', color_code[1])
        draw_vars['node_color'] = color_code[1]


def choose_edge_color():
    print()
    color_code = colorchooser.askcolor(title="Choose Edges Color")
    if color_code[1]:  # Check if a color was chosen
        print('edge_color: ', color_code[1])
        draw_vars['edge_color'] = color_code[1]


def algorithm(G, selected_layout, node_size, node_shape, edge_width, selected_label):
    print()
    global attribute_to_show
    print('selected_layout: ', selected_layout)
    print('node_size: ', node_size)
    print('node_shape: ', node_shape)
    print('edge_width: ', edge_width)

    draw_vars['node_size'] = int(node_size)
    draw_vars['node_shape'] = node_shape
    draw_vars['width'] = int(edge_width)
    attribute_to_show = selected_label

    if selected_layout == "Force-Directed (Fruchterman-Reingold)":
        draw_vars['pos'] = nx.spring_layout(G)
    elif selected_layout == "Hierarchical (Tree)":
        draw_vars['pos'] = graphviz_layout(G, prog='dot')
    elif selected_layout == "Hierarchical (Radial)":
        draw_vars['pos'] = graphviz_layout(G, prog='twopi')
    elif selected_layout == "Eigenvector":
        draw_vars['pos'] = nx.spectral_layout(G)
    elif selected_layout == "Circular":
        draw_vars['pos'] = nx.circular_layout(G)
    elif selected_layout == "Shell":
        draw_vars['pos'] = nx.shell_layout(G)
    elif selected_layout == "Planar":
        draw_vars['pos'] = nx.planar_layout(G)

import networkx as nx
import pydot
from networkx.drawing.nx_pydot import graphviz_layout

layout_options = ["Force-Directed (Fruchterman-Reingold)", "Hierarchical (Tree)",
                  "Hierarchical (Radial)", "Eigenvector", "Circular", "Shell", "Planar"]


def options(G, selected_layout):
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

    return pos

import networkx as nx
from networkx.algorithms import community
from matplotlib import pyplot as plt
import tkinter as tk
from tkinter import ttk
import Graph


G = None
def get_graph():
    global G
    G = Graph.filtered_graph

compare_communities = {
    "Louvain": {
        "Number of Communities": 242,
        "Modularity": 0.284035
    },
    "Girvan-Newman": {
        "Number of Communities": 2,
        "Modularity": -0.000004
    }
}

def run():
    get_graph()
    louvain_comm = louvain()
    girvan_newman_comm = girvan_newman()
    # draw_communities(G, louvain_comm)
    # draw_communities(G, girvan_newman_comm)

def louvain():
    communities = community.louvain_communities(G)
    num_communities = len(set.union(*communities))
    compare_communities(communities, "Louvain", num_communities)
    return communities


def girvan_newman():
    girvan = community.girvan_newman(G)
    #tuple(sorted(c) for c in next(girvan))
    communities = list(next(girvan))
    num_communities = len(communities)
    compare_communities(communities, "Girvan-Newman", num_communities)
    return communities


def compare_communities(communities, algo_name, num_communities):
    print(f"{algo_name}:")
    print(f"\tNumber of Communities: {num_communities}")
    try:
        modularity = community.modularity(G, communities)
        print(f"\tModularity: {modularity:.6f}")
    except:
        print("\tModularity: Not applicable")

def create_gui(data):
    root = tk.Tk()
    root.title("Community Detection Comparison")

    tree = ttk.Treeview(root)
    tree["columns"] = ("Number of Communities", "Modularity")
    tree.heading("#0", text="Method")
    tree.heading("Number of Communities", text="Number of Communities")
    tree.heading("Modularity", text="Modularity")

    for method, values in data.items():
        tree.insert("", "end", text=method, values=(values["Number of Communities"], values["Modularity"]))

    tree.pack(expand=True, fill="both")

    root.mainloop()

def draw_communities(G, communities):
    colors = {}
    for i, community in enumerate(communities):
        for node in community:
            colors[node] = i
    node_colors = [colors[n] for n in G.nodes]
    pos = nx.spring_layout(G)
    nx.draw(G,pos, node_color=node_colors)
    plt.show()




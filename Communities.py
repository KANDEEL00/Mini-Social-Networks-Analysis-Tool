import networkx as nx
from networkx.algorithms import community
from matplotlib import pyplot as plt
import tkinter as tk
from tkinter import ttk
import Graph


G = None
louvain_comm = None
girvan_newman_comm = None
def get_graph():
    global G
    G = Graph.filtered_graph

comparison = {
    "Louvain": {
        "Number of Communities": -1,
        "Modularity": -1
    },
    "Girvan-Newman": {
        "Number of Communities": -1,
        "Modularity": -1
    }
}

def run():
    global louvain_comm, girvan_newman_comm
    get_graph()
    if louvain_comm is None:
        louvain_comm = louvain()
    if girvan_newman_comm is None:
        girvan_newman_comm = girvan_newman()
    create_gui()

def louvain():
    communities = community.louvain_communities(G)
    algo_name = "Louvain"
    comparison[algo_name]['Number of Communities'] = len(set.union(*communities))
    compare_communities(communities, algo_name)
    return communities


def girvan_newman():
    girvan = community.girvan_newman(G)
    communities = list(next(girvan))
    algo_name = "Girvan-Newman"
    comparison[algo_name]['Number of Communities'] = len(communities)
    compare_communities(communities, algo_name)
    return communities


def compare_communities(communities, algo_name):
    comparison[algo_name]['Modularity'] = community.modularity(G, communities)

def create_gui():
    data = comparison
    print("    Louvain    :",data["Louvain"])
    print(" Girvan-Newman :",data["Girvan-Newman"])
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



def draw_both_communities():
    draw_communities(G, louvain_comm, "Louvain")
    draw_communities(G, girvan_newman_comm, "Girvan-Newman")
def draw_communities(G, communities, algo_name):
    colors = {}
    for i, community in enumerate(communities):
        for node in community:
            colors[node] = i
    node_colors = [colors[n] for n in G.nodes]
    pos = nx.spring_layout(G)
    nx.draw(G,pos, node_color=node_colors)
    plt.title(algo_name + " Communities")
    plt.show()



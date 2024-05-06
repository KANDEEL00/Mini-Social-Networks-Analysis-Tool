import networkx as nx
from networkx.algorithms.community import louvain_communities, girvan_newman, modularity
from sklearn.metrics import normalized_mutual_info_score
import tkinter as tk
from tkinter import ttk
from matplotlib import pyplot as plt

import Graph

G = None
louvain_comm = None
girvan_newman_comm = None

comparison = {
    "Louvain": {
        "Number of Communities": -1,
        "Modularity": -.1,
        "NMI": -.1,
        "Conductance": []
    },
    "Girvan-Newman": {
        "Number of Communities": -1,
        "Modularity": -.1,
        "NMI": -.1,
        "Conductance": []
    }
}


def get_graph():
    global G
    G = Graph.filtered_graph


def run():
    global louvain_comm, girvan_newman_comm
    get_graph()
    if louvain_comm is None:
        louvain_comm = calculate_louvain()
    if girvan_newman_comm is None:
        girvan_newman_comm = calculate_girvan_newman()
    show_condutance_table(comparison["Louvain"]["Conductance"], "Louvain")
    show_condutance_table(comparison["Girvan-Newman"]["Conductance"], "Girvan-Newman")
    show_comparison()


def set_comparison_values(communities, algo_name):
    comparison[algo_name]['Number of Communities'] = len(communities)
    comparison[algo_name]['Modularity'] = modularity(G, communities)
    comparison[algo_name]['NMI'] = NMI(communities)
    comparison[algo_name]['Conductance'] = calculate_conductance(communities)

def calculate_louvain():
    communities = louvain_communities(G)
    set_comparison_values(communities, "Louvain")
    return communities

def calculate_girvan_newman():
    girvan = girvan_newman(G)
    communities = list(next(girvan))
    set_comparison_values(communities, "Girvan-Newman")
    return communities

def NMI(partition):
    flat_partition = []
    for i, cluster in enumerate(partition):
        for node in cluster:
            flat_partition.append(i)
    ground_truth_labels = list(nx.get_node_attributes(G, 'Class').values())
    nmi = normalized_mutual_info_score(ground_truth_labels, flat_partition)
    return nmi


def calculate_conductance(communities):
    conductances = []
    for index, community in enumerate(communities):
        conductance = nx.conductance(G, community)
        conductances.append(conductance)
    return conductances


def show_condutance_table(conductance_list, algo_name):
    root = tk.Tk()
    root.title(f"{algo_name} Conductance Values")
    tree = ttk.Treeview(root)
    tree["columns"] = ("Community", "Conductance")
    # Define headings
    tree.heading("#0", text="", anchor=tk.W)
    tree.heading("Community", text="Community", anchor=tk.CENTER)
    tree.heading("Conductance", text="Conductance", anchor=tk.CENTER)
    for community, conductance in enumerate(conductance_list):
        tree.insert("", tk.END, text=algo_name, values=(community, conductance))
    tree.pack(expand=True, fill="both")

def show_comparison():
    data = comparison
    print("    Louvain    :",data["Louvain"])
    print(" Girvan-Newman :",data["Girvan-Newman"])
    root = tk.Tk()
    root.title("Community Detection Comparison")

    tree = ttk.Treeview(root)
    tree["columns"] = ("Number of Communities", "Modularity", "NMI")
    tree.heading("#0", text="Method")
    tree.heading("Number of Communities", text="Number of Communities")
    tree.heading("Modularity", text="Modularity")
    tree.heading("NMI", text="NMI")

    for method, values in data.items():
        tree.insert("", "end", text=method, values=(values["Number of Communities"], values["Modularity"], values["NMI"]))

    tree.pack(expand=True, fill="both")

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

def draw_both_communities():
    draw_communities(G, louvain_comm, "Louvain")
    draw_communities(G, girvan_newman_comm, "Girvan-Newman")


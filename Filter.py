import tkinter as tk
from tkinter import ttk, messagebox
import networkx as nx

import Graph

G = Graph.loaded_graph

# Calculate centrality measures
centrality_measures = {
    'degree': nx.degree_centrality(G),
    'betweenness': nx.betweenness_centrality(G),
    'closeness': nx.closeness_centrality(G)
}


def filter_graph(class_combobox, gender_combobox, centrality_combobox, centrality_scale):
    print()
    selected_class = class_combobox.get()
    selected_gender = gender_combobox.get()
    centrality_measure = centrality_combobox.get()
    centrality_threshold = float(centrality_scale.get())

    filtered_nodes = []
    for node in G.nodes():
        node_class = G.nodes[node]['Class']
        node_gender = G.nodes[node]['Gender']

        # Check if the selected class is 'Any' or matches the node's class
        class_match = selected_class == 'Any' or selected_class == node_class

        # Check if the selected gender is 'Any' or matches the node's gender
        gender_match = selected_gender == 'Any' or selected_gender == node_gender

        if class_match and gender_match:
            centrality_score = centrality_measures[centrality_measure].get(node, 0)
            if centrality_score > centrality_threshold:
                filtered_nodes.append(node)

    Graph.filtered_graph = G.subgraph(filtered_nodes)
    print("\n\n")
    print("Filtered Graph:")
    print("Class:", selected_class)
    print("Gender:", selected_gender)
    print(centrality_measure," threshold: ", centrality_threshold)
    print("Edges:")
    for index, value in enumerate(Graph.filtered_graph.edges()):
        print(f"{index}: {value}")
    print("Nodes:")
    for index, value in enumerate(Graph.filtered_graph.nodes(data=True)):
        print(f"{index}: {value}")

    print("Graph filtered successfully!")
    messagebox.showinfo("Success", "Graph filtered successfully!")


def show_window():
    # Create the main Tkinter window
    root = tk.Tk()
    root.title("Graph Filter GUI")

    # Class selection
    class_label = ttk.Label(root, text="Select Class:")
    class_label.grid(row=0, column=0, padx=10, pady=5)
    class_list = ['Any'] + list(Graph.nodes_df['Class'].unique())
    class_combobox = ttk.Combobox(root, values=class_list)
    class_combobox.grid(row=0, column=1, padx=10, pady=5)
    class_combobox.set('Any')

    # Gender selection
    gender_label = ttk.Label(root, text="Select Gender:")
    gender_label.grid(row=1, column=0, padx=10, pady=5)
    gender_combobox = ttk.Combobox(root, values=['Any', 'M', 'F', 'Unknown'])
    gender_combobox.grid(row=1, column=1, padx=10, pady=5)
    gender_combobox.set('Any')

    # Centrality selection
    centrality_label = ttk.Label(root, text="Select Centrality Measure:")
    centrality_label.grid(row=2, column=0, padx=10, pady=5)
    centrality_combobox = ttk.Combobox(root, values=list(centrality_measures.keys()))
    centrality_combobox.grid(row=2, column=1, padx=10, pady=5)
    centrality_combobox.set(list(centrality_measures.keys())[0])

    # Centrality threshold
    centrality_scale_label = ttk.Label(root, text="Centrality Threshold:")
    centrality_scale_label.grid(row=3, column=0, padx=10, pady=5)
    centrality_scale = ttk.Scale(root, from_=0, to=1, length=200, orient="horizontal")
    centrality_scale.grid(row=3, column=1, padx=10, pady=5)

    # Button to update the graph
    update_button = ttk.Button(root, text="Filter Graph", command=lambda: filter_graph(class_combobox, gender_combobox, centrality_combobox, centrality_scale))
    update_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    root.mainloop()
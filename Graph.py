import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

import Layout

# Create a global variable to store the graph
G = nx.Graph()


# Load the graph from the edges CSV file
def load_edges(file_path_edges, directed_var):
    print()
    print('file_path_edges: ', file_path_edges)
    print('directed_var: ', directed_var.get())
    global G
    try:
        # Read edge CSV with pandas
        df_edges = pd.read_csv(file_path_edges)
        # Create graph based on selected type
        if directed_var.get():
            G = nx.DiGraph()
        else:
            G = nx.Graph()
        G = nx.from_pandas_edgelist(df_edges, 'Source', 'Target')
        G = nx.from_pandas_edgelist(df_edges, 'Source', 'Target', create_using=G)
        print(G.edges())
        return True
    except Exception as e:
        print(f"Failed to load graph: {e}")
        return False


# Load the node attributes from the attributes CSV file
def load_attributes(file_path_attributes):
    print()
    print('file_path_attributes: ', file_path_attributes)
    try:
        # Read node attributes CSV with pandas
        df_attributes = pd.read_csv(file_path_attributes)
        # Add node attributes
        for _, row in df_attributes.iterrows():
            node = row['ID']  # Get the node ID
            for column in df_attributes.columns:
                if column != 'ID':
                    nx.set_node_attributes(G, {node: {column: row[column]}})
        print(G.nodes(data=True))
        return True
    except Exception as e:
        print(f"Failed to load attributes: {e}")
        return False


# Visualize the graph using the selected layout
def visualize_graph():
    print()
    plt.clf()
    label = nx.get_node_attributes(G, Layout.attribute_to_show)
    if Layout.attribute_to_show == 'ID':
        label=None
    nx.draw(G, **Layout.draw_vars, labels=label)
    plt.title('Graph Visualization')
    fig = plt.gcf()
    fig.canvas.manager.set_window_title('Graph Visualization')
    fig.show()
    print('Graph Visualized!!')


def analyze_metrics():
    print()
    metrics = {'num_nodes': nx.number_of_nodes(G),
               'num_edges': nx.number_of_edges(G),
               'degree_distribution': nx.degree_histogram(G),
               'clustering_coefficient': nx.average_clustering(G),
               'average_path_length': 0}
    if nx.is_connected(G):
        metrics['average_path_length'] = nx.average_shortest_path_length(G)
    else:
        metrics['average_path_length'] = "Graph is not connected. Cannot compute average path length."
    output = (
                f"Number of nodes: {metrics['num_nodes']}\n"
                f"Number of edges: {metrics['num_edges']}\n"
                f"Average clustering coefficient: { metrics['clustering_coefficient']}\n"
                f"Average path length: {metrics['average_path_length']}")
    print( "Graph Metrics\n",output)
    print("Degree Distribution")
    for index, value in enumerate(metrics['degree_distribution']):
        print(f"Degree {index}: {value}")
    return metrics
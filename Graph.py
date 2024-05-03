import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

import Layout

# Create a global variable to store the graph
loaded_graph = nx.Graph()
edges_df = None
nodes_df = None
filtered_graph = None


# Load the graph from the edges CSV file
def load_edges(file_path_edges, directed_var):
    print()
    print('file_path_edges: ', file_path_edges)
    print('directed_var: ', directed_var)
    global loaded_graph, edges_df
    try:
        # Read edge CSV with pandas
        edges_df = pd.read_csv(file_path_edges)
        # Create graph based on selected type
        if directed_var:
            loaded_graph = nx.DiGraph()
        else:
            loaded_graph = nx.Graph()
        loaded_graph = nx.from_pandas_edgelist(edges_df, 'Source', 'Target', create_using=loaded_graph)
        print("Loaded Graph:")
        print("Edges:")
        for index, value in enumerate(loaded_graph.edges()):
            print(f"{index}: {value}")
        return True
    except Exception as e:
        print(f"Failed to load graph: {e}")
        return False


# Load the node attributes from the attributes CSV file
def load_attributes(file_path_attributes):
    print()
    print('file_path_attributes: ', file_path_attributes)
    global nodes_df
    try:
        # Read node attributes CSV with pandas
        nodes_df = pd.read_csv(file_path_attributes)
        # Add node attributes
        for _, row in nodes_df.iterrows():
            node = row['ID']  # Get the node ID
            for column in nodes_df.columns:
                if column != 'ID':
                    nx.set_node_attributes(loaded_graph, {node: {column: row[column]}})
        print("Nodes:")
        for index, value in enumerate(loaded_graph.nodes(data=True)):
            print(f"{index}: {value}")
        return True
    except Exception as e:
        print(f"Failed to load attributes: {e}")
        return False


# Visualize the graph using the selected layout
def visualize_graph():
    print()
    plt.clf()
    label = nx.get_node_attributes(filtered_graph, Layout.attribute_to_show)
    if Layout.attribute_to_show == 'ID':
        label = None
    nx.draw(filtered_graph, **Layout.draw_vars, labels=label)
    plt.title('Graph Visualization')
    fig = plt.gcf()
    fig.canvas.manager.set_window_title('Graph Visualization')
    fig.show()
    print('Graph Visualized!!')


def analyze_metrics():
    print()
    metrics = {'num_nodes': nx.number_of_nodes(filtered_graph),
               'num_edges': nx.number_of_edges(filtered_graph),
               'degree_distribution': nx.degree_histogram(filtered_graph),
               'clustering_coefficient': nx.average_clustering(filtered_graph),
               'average_path_length': 0}
    if nx.is_connected(filtered_graph):
        metrics['average_path_length'] = nx.average_shortest_path_length(filtered_graph)
    else:
        metrics['average_path_length'] = "Graph is not connected. Cannot compute average path length."
    output = (
                f"Number of nodes: {metrics['num_nodes']}\n"
                f"Number of edges: {metrics['num_edges']}\n"
                f"Average clustering coefficient: { metrics['clustering_coefficient']}\n"
                f"Average path length: {metrics['average_path_length']}")
    print("Graph Metrics\n", output)
    print("Degree Distribution")
    for index, value in enumerate(metrics['degree_distribution']):
        print(f"Degree {index}: {value}")
    return metrics

import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

# Create a global variable to store the graph
G = nx.Graph()


# Load the graph from the edges CSV file
def load_edges(file_path_edges, directed_var):
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
def visualize_graph(pos):
    plt.clf()
    draw_vars = {
        'pos': pos,
        'with_labels': True,
        'node_size': 1000,
        'node_color': '#ff0000',
        'node_shape': 'o',
        'width': 1,
        'edge_color': '#0000ff',
        'arrows': True,
        'alpha': 1,
    }
    nx.draw(G, **draw_vars)
    plt.title('Graph Visualization')
    fig = plt.gcf()
    fig.canvas.manager.set_window_title('Graph Visualization')
    fig.show()

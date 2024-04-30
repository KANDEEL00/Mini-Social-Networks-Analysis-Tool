import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

G = nx.DiGraph()

def load_graph():
    global G
    file_path_edges = filedialog.askopenfilename(title="Open Edges CSV File",filetypes=[("CSV Files", "*.csv")])
    if file_path_edges:
        try:
            # Read edge CSV with pandas
            df_edges = pd.read_csv(file_path_edges)
            # Create a graph from pandas DataFrame
            G = nx.from_pandas_edgelist(df_edges, 'Source', 'Target',create_using=G)
            print(G.edges())
            # Ask for node attributes CSV
            file_path_attributes = filedialog.askopenfilename(title="Open Nodes CSV File",filetypes=[("CSV Files", "*.csv")])
            if file_path_attributes:
                # Read node attributes CSV with pandas
                df_attributes = pd.read_csv(file_path_attributes)

                # Add node attributes
                for _, row in df_attributes.iterrows():
                    node = row['ID']  # Adjusted to 'ID' column
                    for column in df_attributes.columns:
                        if column != 'ID':  # Adjusted to 'ID' column
                            nx.set_node_attributes(G, {node: {column: row[column]}})
                print(G.nodes(data=True))
                update_button.config(state=tk.NORMAL)
                messagebox.showinfo("Success", "Graph loaded successfully!")
            else:
                messagebox.showwarning("Warning", "No node attributes file selected.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load graph: {e}")


def update_graph():
    global row
    plt.clf()
    nx.draw(G, with_labels=True, node_color='lightblue', node_size=500)
    plt.title('Graph Visualization')
    fig = plt.gcf()
    fig.canvas.manager.set_window_title('Graph Visualization')
    fig.show()

# Create the main window
window = tk.Tk()
window.geometry("400x200")
window.title('Mini Social Networks Analysis Tool')
row= 0
# Create the load button
load_button = ttk.Button(window, text='Load Graph', command=load_graph)
load_button.grid(row=row, columnspan=2, pady=10)
row += 1
# Create the update button
update_button = ttk.Button(window, text='Update Graph', command=update_graph, state=tk.DISABLED)
update_button.grid(row=row, columnspan=2, pady=10)
row += 1
# Run the main event loop
window.mainloop()

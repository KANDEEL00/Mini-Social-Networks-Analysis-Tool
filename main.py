import tkinter as tk
from tkinter import ttk, filedialog, messagebox, StringVar
import networkx as nx

import matplotlib.pyplot as plt
import pandas as pd

import Layout

# Create a global variable to store the graph
G = None

def load_graph():
    global G
    file_path_edges = filedialog.askopenfilename(title="Open Edges CSV File", filetypes=[("CSV Files", "*.csv")])
    if file_path_edges:
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
            # Ask for node attributes CSV
            file_path_attributes = filedialog.askopenfilename(title="Open Nodes CSV File", filetypes=[("CSV Files", "*.csv")])
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
    pos = Layout.options(G, selected_layout.get())
    plt.clf()
    nx.draw(G, with_labels=True, pos=pos, node_color='lightblue', node_size=500)
    plt.title('Graph Visualization')
    fig = plt.gcf()
    fig.canvas.manager.set_window_title('Graph Visualization')
    fig.show()


# Create the main window
window = tk.Tk()
window.geometry("400x200")
window.title('Mini Social Networks Analysis Tool')

# Create a variable to store the state of the checkbox
directed_var = tk.BooleanVar(value=False)

row = 0

# Create the checkbox for directed/undirected graph
checkbox = ttk.Checkbutton(window, text="Directed Graph", variable=directed_var)
checkbox.grid(row=row, column=0, pady=10)
# Create the load button
load_button = ttk.Button(window, text='Load Graph', command=load_graph)
load_button.grid(row=row, column=1, pady=10)# Now define variables that rely on the root window
selected_layout = StringVar(window)  # Define selected_layout after creating root
selected_layout.set(Layout.layout_options[0])  # Set default layout
row += 1

# Create the layout label
layout_label = ttk.Label(window, text="Layout: ")
layout_label.grid(row=row, column=0, pady=10)
# Create the layout dropdown
layout_menu = ttk.Combobox(window, textvariable=selected_layout, state="readonly", width=30)
layout_menu["values"] = Layout.layout_options
layout_menu.grid(row=row, column=1, pady=10)
row += 1

# Create the update button
update_button = ttk.Button(window, text='Update Graph', command=update_graph, state=tk.DISABLED)
update_button.grid(row=row, columnspan=2, pady=10)
row += 1
# Run the main event loop
window.mainloop()

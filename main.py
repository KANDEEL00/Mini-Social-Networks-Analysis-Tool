import tkinter as tk
from tkinter import ttk, filedialog, messagebox, StringVar, Label, Entry
import Layout
import Graph
import Filter
import Communities


def load_graph():
    file_path_edges = filedialog.askopenfilename(title="Open Edges CSV File", filetypes=[("CSV Files", "*.csv")])
    if file_path_edges:
        try:
            Graph.load_edges(file_path_edges, directed_var.get())
            file_path_attributes = filedialog.askopenfilename(title="Open Nodes CSV File", filetypes=[("CSV Files", "*.csv")])
            if file_path_attributes:
                Graph.load_attributes(file_path_attributes)
                Graph.filtered_graph = Graph.loaded_graph
                metrics_button.config(state=tk.NORMAL)
                link_analysis_button.config(state=tk.NORMAL)
                filter_graph_button.config(state=tk.NORMAL)
                comm_graph_button.config(state=tk.NORMAL)
                visualize_graph_button.config(state=tk.NORMAL)
                print('Graph loaded successfully!')
                messagebox.showinfo("Success", "Graph loaded successfully!")
            else:
                print('No node attributes file selected.')
                messagebox.showwarning("Warning", "No node attributes file selected.")
        except Exception as e:
            print(f"Failed to load graph: {e}")
            messagebox.showerror("Error", f"Failed to load graph: {e}")


def analyze_metrics():
    metrics = Graph.analyze_metrics()
    messagebox.showinfo("Graph Metrics", f"Number of nodes: {metrics['num_nodes']}\n"
                                                      f"Number of edges: {metrics['num_edges']}\n"
                                                      f"Average clustering coefficient: { metrics['clustering_coefficient']}\n"
                                                      f"Average path length: {metrics['average_path_length']}")

def link_analysis():
    Graph.link_analisys()
def filter_graph():
    Filter.show_window()
def community_detection():
    Communities.run()
    draw_comm_graph_button.config(state=tk.NORMAL)

def draw_communities():
    Communities.draw_both_communities()
def visualize_graph():
    Layout.algorithm(Graph.filtered_graph, selected_layout.get(), node_size_entry.get(), selected_shape.get(), edge_width_entry.get(), selected_label.get())
    Graph.visualize_graph()


# Create the main window
window = tk.Tk()
window.geometry("800x225")
window.title('Mini Social Networks Analysis Tool')
row = 0

# Create the checkbox for directed/undirected graph
directed_var = tk.BooleanVar(value=False) # Create a BooleanVar to store the checkbox state
checkbox = ttk.Checkbutton(window, text="Directed Graph", variable=directed_var)
checkbox.grid(row=row, column=0, pady=10 , padx=10)

# load button
load_button = ttk.Button(window, text='Load Graph', command=load_graph)
load_button.grid(row=row, column=1, pady=10 , padx=10)
# metrics button
metrics_button = ttk.Button(window, text='Show Metrics and Statistics', command=analyze_metrics, state=tk.DISABLED)
metrics_button.grid(row=row, column=2, pady=10 , padx=10)
# Layout Selection
selected_layout = StringVar(window)  # Create a StringVar to store the selected layout
selected_layout.set(Layout.layout_options[0])  # Set the default layout
layout_label = ttk.Label(window, text="Layout Algorithm:  ")
layout_label.grid(row=row, column=3, pady=10 , padx=10, sticky="E")
# Layout dropdown
layout_menu = ttk.Combobox(window, textvariable=selected_layout, state="readonly")
layout_menu["values"] = Layout.layout_options
layout_menu.grid(row=row, column=4, pady=10, padx=10, sticky="W")
row += 1

# Node Row
# Node Size Label
node_size_label = Label(window, text="Node Size:  ")
node_size_label.grid(row=row, column=0, pady=10, padx=10,sticky="E")
# Node Size Entry
node_size_entry = Entry(window)
node_size_entry.insert(0, str(Layout.draw_vars['node_size']))
node_size_entry.grid(row=row, column=1, pady=10, padx=10,sticky="W")
# Node Color Button
node_color_button = ttk.Button(window, text="Choose Node Color", command=Layout.choose_node_color)
node_color_button.grid(row=row, column=2, pady=10 , padx=10, sticky="W")
# Node Shape Label
selected_shape = StringVar(window)
selected_shape.set(Layout.draw_vars['node_shape'])
shape_label = ttk.Label(window, text="Node Shape:  ")
shape_label.grid(row=row, column=3, pady=10 , padx=10, sticky="E")
# Layout dropdown
shape_menu = ttk.Combobox(window, textvariable=selected_shape, state="readonly")
shape_menu["values"] = ['o', 's', '^', 'v', '<', '>']
shape_menu.grid(row=row, column=4, pady=10 , padx=10, sticky="W")
row += 1

# Edge Row
# Edge Width Row
edge_width_label = Label(window, text="Edge Width:")
edge_width_label.grid(row=row, column=0,pady=10, padx=10, sticky="E")
# Edge Width Entry
edge_width_entry = Entry(window)
edge_width_entry.insert(0, str(Layout.draw_vars['width']))
edge_width_entry.grid(row=row, column=1,pady=10, padx=10, sticky="W")
# Edge Color
edge_color_button = ttk.Button(window, text="Choose Edge Color", command=Layout.choose_edge_color)
edge_color_button.grid(row=row, column=2, pady=10, padx=10, sticky="W")

# Node Label
selected_label = StringVar(window)
selected_label.set('ID')
label_label = ttk.Label(window, text="Node Label:  ")
label_label.grid(row=row, column=3, pady=10 , padx=10, sticky="E")
# Layout dropdown
lable_menu = ttk.Combobox(window, textvariable=selected_label, state="readonly")
lable_menu["values"] = ['ID','Class','Gender']
lable_menu.grid(row=row, column=4, pady=10 , padx=10, sticky="W")
row += 1

# Create the update button
link_analysis_button = ttk.Button(window, text='Link Analysis', command=link_analysis, state=tk.DISABLED)
link_analysis_button.grid(row=row, column=0, pady=10, padx=10)
filter_graph_button = ttk.Button(window, text='Filter Graph', command=filter_graph, state=tk.DISABLED)
filter_graph_button.grid(row=row, column=1, pady=10, padx=10)
comm_graph_button = ttk.Button(window, text='Community Detection \n     & Comparison', command=community_detection, state=tk.DISABLED)
comm_graph_button.grid(row=row, column=2, pady=10, padx=10)
draw_comm_graph_button = ttk.Button(window, text='Graph Partitioning', command=draw_communities, state=tk.DISABLED)
draw_comm_graph_button.grid(row=row, column=3, pady=10, padx=10)
visualize_graph_button = ttk.Button(window, text='Visualize Graph', command=visualize_graph, state=tk.DISABLED)
visualize_graph_button.grid(row=row, column=4, pady=10, padx=10)
row += 1

# Run the main event loop
window.mainloop()

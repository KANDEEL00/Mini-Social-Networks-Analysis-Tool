import tkinter as tk
from tkinter import ttk, filedialog, messagebox, StringVar
import Layout
import Graph

def load_graph():
    file_path_edges = filedialog.askopenfilename(title="Open Edges CSV File", filetypes=[("CSV Files", "*.csv")])
    if file_path_edges:
        try:
            Graph.load_edges(file_path_edges, directed_var)
            file_path_attributes = filedialog.askopenfilename(title="Open Nodes CSV File", filetypes=[("CSV Files", "*.csv")])
            if file_path_attributes:
                Graph.load_attributes(file_path_attributes)
                visualize_graph_button.config(state=tk.NORMAL)
                print('Graph loaded successfully!')
                messagebox.showinfo("Success", "Graph loaded successfully!")
            else:
                print('No node attributes file selected.')
                messagebox.showwarning("Warning", "No node attributes file selected.")
        except Exception as e:
            print(f"Failed to load graph: {e}")
            messagebox.showerror("Error", f"Failed to load graph: {e}")

def visualize_graph():
    Graph.visualize_graph(selected_layout.get())


# Create the main window
window = tk.Tk()
window.geometry("400x200")
window.title('Mini Social Networks Analysis Tool')
row = 0

# Create the checkbox for directed/undirected graph
directed_var = tk.BooleanVar(value=False) # Create a BooleanVar to store the checkbox state
checkbox = ttk.Checkbutton(window, text="Directed Graph", variable=directed_var)
checkbox.grid(row=row, column=0, pady=10)

# Create the load button
load_button = ttk.Button(window, text='Load Graph', command=load_graph)
load_button.grid(row=row, column=1, pady=10)
row += 1

# Create the layout label
selected_layout = StringVar(window)  # Create a StringVar to store the selected layout
selected_layout.set(Layout.layout_options[0])  # Set the default layout
layout_label = ttk.Label(window, text="Layout: ")
layout_label.grid(row=row, column=0, pady=10)

# Create the layout dropdown
layout_menu = ttk.Combobox(window, textvariable=selected_layout, state="readonly", width=30)
layout_menu["values"] = Layout.layout_options
layout_menu.grid(row=row, column=1, pady=10)
row += 1

# Create a button to open the color picker
choose_button = tk.Button(window, text="Choose Node Color", command=Layout.choose_node_color)
choose_button.grid(row=row, column=1, pady=10)
row += 1

# Create the update button
visualize_graph_button = ttk.Button(window, text='Visualize Graph', command=visualize_graph , state=tk.DISABLED)
visualize_graph_button.grid(row=row, columnspan=2, pady=10)
row += 1

# Run the main event loop
window.mainloop()

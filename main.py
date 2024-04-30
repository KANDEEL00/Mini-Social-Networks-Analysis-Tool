import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

G = nx.Graph()
def load_graph():
    global G
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if file_path:
        try:
            # Read CSV with pandas
            df = pd.read_csv(file_path)
            # Create a graph from pandas DataFrame
            G = nx.from_pandas_edgelist(df, 'Source', 'Target')
            update_button.config(state=tk.NORMAL)
            messagebox.showinfo("Success", "Graph loaded successfully!")
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

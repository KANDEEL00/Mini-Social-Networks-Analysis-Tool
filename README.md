# Mini Social Networks Analysis Tool

## Overview

The Mini Social Networks Analysis Tool is a desktop software designed for network analysis and visualization. It serves as a versatile tool for data analysts and researchers to delve into graphs representing diverse networks. Users can interact with the graphs extensively, such as adjusting node and edge properties, filtering based on various criteria, applying different community detection methods, and employing link prediction techniques. This tool is aimed at providing a comprehensive platform for exploring and understanding network structures efficiently.

## Features

1. **Node and Edge Attributes**: Users can define and visualize custom attributes for nodes and edges, including size, color, label, and shape.
   
2. **Layout Algorithms**: Various layout algorithms are implemented to visualize network structures differently, including force-directed algorithms like Fruchterman-Reingold and hierarchical layouts such as tree or radial layouts.
   
3. **Graph Metrics and Statistics**: Integration of a wide range of graph metrics and statistics to analyze network properties and characteristics, covering basic metrics like degree distribution, clustering coefficient, and average path length.
   
4. **Filtering Options**: 
   - Filtering nodes based on centrality measures (at least three centrality measures).
   - Filtering nodes based on their membership in specific communities or their centrality scores within certain ranges.
   
5. **Community Detection Comparison**: Comparison of results from different community detection algorithms such as Girvan Newman and Louvain algorithm, displaying metrics like the number of communities detected and modularity scores side by side.
   
6. **Graph Partitioning and Clustering**: Implementation of algorithms for partitioning the graph into clusters or communities based on various criteria.
   
7. **Clustering Evaluation**: Application of at least 3 community detection evaluations (internal and external evaluation).
   
8. **Basic Visualization**: Provides basic visualization of network structures.
   
9. **Link Analysis Techniques**: Implementation of various link analysis techniques like PageRank and Betweenness Centrality to analyze relationships between nodes and identify important nodes and relationships within the network.

## Usage

The tool allows users to load network data from two CSV files: one for nodes and one for edges. It supports both directed and undirected graphs.

## Implementation Details

The Mini Social Networks Analysis Tool can be implemented using any programming language, although Python (NetworkX) is recommended. It is designed as a GUI desktop application, but can also be implemented as a web application for flexibility.

## Dependencies

- Python (with NetworkX library)
- GUI framework (if developing desktop application)
- Web development framework (if developing web application)

## Installation

1. Clone or download the repository.
2. Install the required dependencies.
3. Run the application.

## Contributing

Contributions are welcome! Please feel free to fork the repository and submit pull requests to contribute to the project.

## License

This project is licensed under the [MIT License](LICENSE).

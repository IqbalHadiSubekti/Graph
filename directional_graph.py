#!/usr/bin/env python
# -*- coding: utf-8 -*-
import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph() #or G = nx.MultiDiGraph()

#add nodes
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)

#add edges
G.add_edge(1, 1, length = 0)
G.add_edge(1, 2, length = 10)
G.add_edge(1, 3, length = 15)
G.add_edge(1, 4, length = 20)

G.add_edge(2, 1, length = 5)
G.add_edge(2, 2, length = 0)
G.add_edge(2, 3, length = 9)
G.add_edge(2, 4, length = 12)

G.add_edge(3, 1, length = 6)
G.add_edge(3, 2, length = 13)
G.add_edge(3, 3, length = 0)
G.add_edge(3, 4, length = 12)

G.add_edge(4, 1, length = 8)
G.add_edge(4, 2, length = 8)
G.add_edge(4, 3, length = 9)
G.add_edge(4, 4, length = 0)

#position nodes
pos = nx.spring_layout(G)

#drawing graph
nx.draw(G, pos, with_labels=True)
edge_labels=dict([((u,v,),d['length'])
				for u,v,d in G.edges(data=True)])
				
#drawing edge labels
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels,
								
								
								
								
								
								
								
								label_pos=0.3, font_size=7)

nx.draw_networkx_edges(G, pos,
						edgelist=[(1,3),(3,4),(4,2),(2,1)],
						width=2,alpha=0.5,edge_color='b')	
plt.show()
						











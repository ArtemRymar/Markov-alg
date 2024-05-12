import networkx as nx
import matplotlib.pyplot as plt



# def find_combinations(target, arr, prefix="", result=[]):
#     if not target:
#         result.append(prefix)
#         return
#     for word in arr:
#         if target.startswith(word):
#             find_combinations(target[len(word):], arr, prefix + word, result)

# string1 = "010"
# arr = ["01", "010", "0", "1001"]

# st = ""
# end = ''




# G = nx.MultiDiGraph()

# node = [0, 1, 2, 3, 4]

# G.add_nodes_from(node)


# G.add_edge(0, 1, key = 1)
# G.add_edge(1, 0, key=2)

# pos = nx.circular_layout(G)
# nx.draw(G, pos, with_labels=True, node_size=1000, node_color="white",edgecolors="black", font_size=12, font_weight="bold", arrowsize=20)

# edge_labels = nx.get_edge_attributes(G, 'name')
# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)


# plt.show()



    

G = nx.DiGraph()

# Add two edges between nodes 1 and 2
G.add_node(1)
G.add_node(2)


# Добавление ребер
G.add_edge(1, 2, name='01')
G.add_edge(2,3, name='lol')
G.add_edge(2, 1, name='0001')


# Отрисовка графа с искривленными ребрами
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=300, node_color="skyblue")


curveEdges = []
straightEdges = []

for u,v in G.edges():
    if (u,v) in G.edges() and (v,u) in G.edges():
        if (u,v) not in curveEdges:
            curveEdges.append((u,v))
        if (v,u) not in curveEdges:
            curveEdges.append((v,u))
    elif (u,v) in G.edges():
        straightEdges.append((u,v))
    elif (v,u) in G.edges():
        straightEdges.append((v,u))

print(curveEdges)
print(straightEdges)




edge_labels = nx.get_edge_attributes(G, "name")
edge_labels[(1,2,0)] = '10'
nx.draw_networkx_edge_labels(G, pos,edge_labels=edge_labels, connectionstyle="arc3,rad=0.12")
edgesc = nx.draw_networkx_edges(G, pos,edgelist=curveEdges, connectionstyle="arc3,rad=0.2")
edgess = nx.draw_networkx_edges(G, pos, edgelist=straightEdges)

edge_labels[(1,2,0)] = '10'
print(edge_labels)






plt.show()
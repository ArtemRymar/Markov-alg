import networkx as nx
import matplotlib.pyplot as plt


def isSuffAndPostf(code, substr):
    isSuf = False
    isPostf = False

    for word in code:
        if word.startswith(substr, 0, -1) == True:
            isSuf = True
        if word.endswith(substr, 1) == True:
            isPostf = True
    
    if isSuf == True and isPostf == True:
        return True
    else:
        return False
    


def findElementaryDecompositions(target, arr, prefix="", result=[], count=0):
    if not target:
        result.append(prefix)
        return
    for word in arr:
        if target.startswith(word):
            findElementaryDecompositions(target[len(word):], arr, prefix + word, result)
            count += 1







if __name__ == '__main__':

    V = []
    
    str = input("Input the alphabet: ")
    V = str.replace(',', '').split(' ')
    


    S1 = []
    for code in V:
        n = len(code)
        for i in range(1,n):
            substr = code[:i]   
            if substr not in S1 and isSuffAndPostf(V, substr):
                S1.append(substr)

                
    Sl = S1 + ['λ']
    S = S1 + ['']

    G = nx.MultiDiGraph()

    for each in Sl:
        G.add_node(each)


   
    for word in V:
        for start in S:
            for end in S:
                if start != '' and end != '' and start + end == word:
                    G.add_edge(start, end, name='λ')
                elif word.startswith(start, 0, len(word)-1) and word.endswith(end, 1):
                    counter = 0
                    nameOfEdge = []
                    findElementaryDecompositions(word[len(start):len(word)-len(end)], V, "", nameOfEdge, counter)
                    if len(nameOfEdge) != 0 and nameOfEdge[0] != '':    
                        if start == end and start != '':
                            G.add_edge(start, end, name = nameOfEdge[0])
                        elif start == '' and start == end:
                            if counter > 1:
                                G.add_edge('λ', 'λ', name=nameOfEdge[0])
                        else:
                            if start == '':
                                G.add_edge('λ', end, name=nameOfEdge[0])
                            elif end == '':
                                G.add_edge(start, 'λ', name=nameOfEdge[0])
                            else:
                                G.add_edge(start, end, name=nameOfEdge[0])
                            


                
    cycles = nx.simple_cycles(G)

    cycleThrowLambda = None
    lenmax = 10000

    for cycle in cycles:
        if 'λ' in cycle:
            if len(cycle) < lenmax:
                cycleThrowLambda = cycle
                lenmax = len(cycle)

    print("Найден цикл:", cycleThrowLambda)


    curveEdges = []
    straightEdges = []
    edge_labels = nx.get_edge_attributes(G, 'name')

    for u,v in G.edges():
        if (u,v) in G.edges() and (v,u) in G.edges() :
            if (u,v) not in curveEdges:
                curveEdges.append((u,v))
            if (v,u) not in curveEdges:
                curveEdges.append((v,u))
        elif (u,v) in G.edges():
            if (u,v) not in straightEdges:
                straightEdges.append((u,v))
        elif (v,u) in G.edges():
            if (v,u) not in straightEdges:
                straightEdges.append((v,u))
            

   
   
   
    pos = nx.circular_layout(G)
    edge_colors = ['blue' if u in cycleThrowLambda and v in cycleThrowLambda and u!= v else 'black' for u, v in G.edges()]
    
    nx.draw(G, pos, with_labels=True, node_size=1000, node_color="white", edgecolors='black', font_size=12, font_weight="bold", arrowsize=10)
    # nx.draw_networkx_edges(G, pos, edge_color=edge_colors)
    # nx.draw_networkx_nodes(G, pos, node_size=1000, node_color="white")
    nx.draw_networkx_edges(G, pos,edgelist=curveEdges, connectionstyle="arc3,rad=0.2",edge_color=edge_colors)
    nx.draw_networkx_edges(G, pos, edgelist=straightEdges, edge_color=edge_colors)

    

    edge_labels = nx.get_edge_attributes(G, 'name')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, connectionstyle="arc3,rad=0.12")


    plt.show()


    
    print(S)
    for u, v, data in G.edges(data=True):
        names = data
        print(f"Edge from {u} to {v}, name: {names}")

    

    print(edge_labels)


  

    
        
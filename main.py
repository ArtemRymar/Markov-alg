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

    G = nx.DiGraph()

    for each in Sl:
        G.add_node(each)

    edge_colors = nx.get_edge_attributes(G, 'color')
   
    for word in V:
        for start in S:
            for end in S:
                if start != '' and end != '' and start + end == word:
                    G.add_edge(start, end, name='λ', color='black')
                elif word.startswith(start, 0, len(word)-1) and word.endswith(end, 1):
                    counter = 0
                    nameOfEdge = []
                    findElementaryDecompositions(word[len(start):len(word)-len(end)], V, "", nameOfEdge, counter)
                    if len(nameOfEdge) != 0 and nameOfEdge[0] != '':    
                        if start == end and start != '':
                            G.add_edge(start, end, name = nameOfEdge[0], color='black')
                        elif start == '' and start == end:
                            if counter > 1:
                                G.add_edge('λ', 'λ', name=nameOfEdge[0], color='black')
                        else:
                            if start == '':
                                G.add_edge('λ', end, name=nameOfEdge[0], color='black')
                            elif end == '':
                                G.add_edge(start, 'λ', name=nameOfEdge[0], color='black')
                            else:
                                G.add_edge(start, end, name=nameOfEdge[0], color='black')
                            


                
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
    

    # for i in range(1,len(cycleThrowLambda)):
    #     edge_colors[(cycleThrowLambda[i-1], cycleThrowLambda[i])] = 'blue'
    # edge_colors[('λ', '0')] = ''
        

    for u,v in G.edges():
        if (u,v) in G.edges() and (v,u) in G.edges() and edge_labels[(u,v)] != edge_labels[(v,u)]:
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
    #edge_colors = ['blue' if u in cycleThrowLambda and v in cycleThrowLambda and u!= v else 'black' for u, v in G.edges()]
    # edge_colors1 = ['blue' if u in cycleThrowLambda and v in cycleThrowLambda and u!= v and ((u,v) in curveEdges or (v,u) in curveEdges) else 'black' for u, v in G.edges()]
    # edge_colors2 = ['blue' if u in cycleThrowLambda and v in cycleThrowLambda and u!= v and ((u,v) in straightEdges or (v,u) in straightEdges) else 'black' for u, v in G.edges()]
    nx.draw(G, pos, with_labels=True, node_size=1000, node_color="white", edgecolors='black', font_size=12, font_weight="bold", width=0, arrowsize=0)

    
    nx.draw_networkx_edges(G, pos,edgelist=curveEdges, connectionstyle="arc3,rad=0.15",edge_color=edge_colors, arrowsize=13, node_size=1000)
    nx.draw_networkx_edges(G, pos, edgelist=straightEdges, edge_color=edge_colors, width=1, arrowsize=13, node_size=1000)

   
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u,v):edge_labels[(u,v)] for (u,v) in curveEdges}, connectionstyle="arc3,rad=0.16")
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u,v):edge_labels[(u,v)] for (u,v) in straightEdges}, connectionstyle="arc3")
    
    
    # print(edge_colors)
    print(G.edges)
    print(edge_colors)


    plt.show()





  

    
        
#! /usr/bin/env python3


from Bio import pairwise2
import networkx as nx
import matplotlib.pyplot as plt


class Align_Class:
    def __init__(self, name, threshold):
        self.filename = name
        self.SeqList = []
        self.HeadList = []
        self.ScoreList = []
        self.threshold = threshold

    def FastaDic(self):
        FileName = open(self.filename,'r')
        self.fastaDict = {}
        for line in FileName:
            if line[0]=='>':
                header = line[1:]
                print(header)
                #header = header[:25]
                print(header+'\n'+'\n')
                self.fastaDict[header]=''
            else:
                self.fastaDict[header]+=line.rstrip()
        FileName.close()
        return self.fastaDict

    def MakeSeqList(self):
        self.SeqList = [val for val in self.fastaDict.values()]

    def MakeHeadList(self):
        self.HeadList = [header for header in self.fastaDict.keys()]

    def Make_Graph(self):
        tuple=()
        score_align=0
        ScoreNoeud = []
        
        # add nodes + add edged
        self.GraphSeq = nx.Graph()
        for i in range(len(self.HeadList)):
            scorelist = []
            self.GraphSeq.add_node(self.HeadList[i])
            for j in range(i+1, len(self.HeadList)):
                score_align=pairwise2.align.globalxx(self.HeadList[i],self.HeadList[j],score_only=True)
                scorelist.append(score_align)
                #tuple=(self.HeadList[i],self.HeadList[j],score_align)
                if (score_align>self.threshold):
                    self.GraphSeq.add_edge(self.HeadList[i],self.HeadList[j],weight = score_align)
            ScoreNoeud.append(sum(scorelist))
        weights = nx.get_edge_attributes(self.GraphSeq,'weight').values()
        maxou = max(list(weights))
        minou = min(list(weights))
        weights = [((i-minou)/(maxou-minou))*11 for i in list(weights)]
        maxou = max(ScoreNoeud)
        minou = min(ScoreNoeud)
        ScoreNoeud = [((i-minou)/(maxou-minou))*11 for i in ScoreNoeud]
        
        pos = nx.spring_layout(self.GraphSeq)
        
        
        #with_labels=True
        nx.draw(self.GraphSeq, pos, width=weights, edge_color = weights, edge_cmap=plt.cm.magma, node_color=ScoreNoeud, cmap=plt.cm.magma)
        
        #afficher les valeurs de score sur les arcs
        edge_labels = nx.get_edge_attributes(self.GraphSeq,'weight')
        nx.draw_networkx_edge_labels(self.GraphSeq, pos, edge_labels = edge_labels)
        
        #afficher le nom des noeuds, manque l'attribut
        #node_labels = nx.get_node_attributes(self.GraphSeq,'state')
        #nx.draw_networkx_labels(self.GraphSeq, pos, labels = node_labels)
        
        
        
        plt.show()

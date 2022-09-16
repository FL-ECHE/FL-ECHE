#! /usr/bin/env python3

import sys
from Generator import Random_Fasta
from AlignClass import Align_Class
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QPushButton, QWidget, QApplication, QGridLayout, QLabel, QLineEdit, QFileDialog

class Window(QWidget):
    def __init__(self):
        super().__init__()
        #setting up the layout of the window
        layout = QGridLayout()
        self.setWindowTitle("AlignGraphMaker")
        self.setLayout(layout)

        title = QLabel("Sequence Alignment Graph")
        layout.addWidget(title, 0,1)
        filen = QLabel("Filename will be selected after CREATE button")
        layout.addWidget(filen,1,0)
        thr = QLabel("Threshold :")
        layout.addWidget(thr,2,0)
        
        #Setting up inputs
        self.input1 = QFileDialog()
        #layout.addWidget(self.input1, 1,1)
        self.input2 = QLineEdit("insert min value here")
        layout.addWidget(self.input2,2,1)
        
        #establishing the action when the from is complete
        btn1 = QPushButton("create")
        btn1.clicked.connect(self.construct)
        layout.addWidget(btn1,3,2)

        #list of inputs for random sequence generation
        self.input3 = QLineEdit("generated sequence lenght")
        self.input4 = QLineEdit("number of generated sequences")
        layout.addWidget(self.input3,4,1)
        layout.addWidget(self.input4,5,1)
        


        #authorizing the use of random sequences generated
        btn2 = QPushButton("use random sequences")
        btn2.clicked.connect(self.generate)
        layout.addWidget(btn2,6,2)
    
    def construct(self):
        #calls the AlignClass library to construct and show the graph
        graph = Align_Class(self.input1.getOpenFileName(caption='Select Fasta File')[0],int(self.input2.text()))
        graph.FastaDic()
        graph.MakeSeqList()
        graph.MakeHeadList()
        graph.Make_Graph()
        

    def generate(self):
        genero = Random_Fasta(self.input3.text(), self.input4.text())
        genero.create()
        graph = Align_Class("random.fasta",0)
        graph.FastaDic()
        graph.MakeSeqList()
        graph.MakeHeadList()
        graph.Make_Graph()
        


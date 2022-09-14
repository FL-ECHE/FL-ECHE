#! /usr/bin/env python3

import sys
from AlignClass import Align_Class
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QPushButton, QWidget, QApplication, QGridLayout, QLabel, QLineEdit

class Window(QWidget):
    def __init__(self):
        super().__init__()
        #setting up the layout of the window
        layout = QGridLayout()
        self.setWindowTitle("AlignGraphMaker")
        self.setLayout(layout)

        title = QLabel("Sequence Alignment Graph")
        layout.addWidget(title, 0,1)
        user = QLabel("File :")
        layout.addWidget(user,1,0)
        pwd = QLabel("Threshold :")
        layout.addWidget(pwd,2,0)
        
        #Setting up inputs
        self.input1 = QLineEdit("insert filepath here")
        layout.addWidget(self.input1, 1,1)
        self.input2 = QLineEdit("insert min value here")
        layout.addWidget(self.input2,2,1)
        
        #establishing the action when the from is complete
        btn1 = QPushButton("create")
        btn1.clicked.connect(self.construct)
        layout.addWidget(btn1,3,2)
    
    def construct(self):
        #calls the AlignClass library to construct and show the graph
        graph = Align_Class(self.input1.text(),int(self.input2.text()))
        graph.FastaDic()
        graph.MakeSeqList()
        graph.MakeHeadList()
        graph.Make_Graph()



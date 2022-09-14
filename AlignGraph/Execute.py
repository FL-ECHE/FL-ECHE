#! /usr/bin/env python3

from AlignClass import Align_Class

graph = Align_Class("test.fasta", 0)
graph.FastaDic()
graph.MakeSeqList()
graph.MakeHeadList()
graph.Make_Graph()

#! /usr/bin/env python3 

from Bio import SeqIO
import random

aaList = ['A','C','D','E','F','H','I','K','L','M','N','P','Q','R','S','T','V','W']
#SeqIO.write(sequences, "random.fasta", "fasta")

class Random_Fasta:
    def __init__(self, lenght, howmuch):
        self.longu = lenght
        self.nombu = howmuch

    def create(self):
        sequences = []
        for i in range(0,int(self.nombu)):
            seq = ""
            for i in range(0,int(self.longu)):
                seq += aaList[random.randint(0,17)]
            sequences.append(seq)

        SeqIO.write(sequences, "random.fasta", "fasta")



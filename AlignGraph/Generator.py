#! /usr/bin/env python3 

from Bio import SeqIO, SeqRecord, Seq
import random

aaList = ['A','C','D','E','F','H','I','K','L','M','N','P','Q','R','S','T','V','W','G','Y']
#SeqIO.write(sequences, "random.fasta", "fasta")

class Random_Fasta:
    def __init__(self, lenght, howmuch):
        self.longu = lenght
        self.nombu = howmuch

    def create(self):
        sequences = []
        for i in range(0,int(self.nombu)):
            seq = ""
            for j in range(0,int(self.longu)):
                seq += aaList[random.randint(0,19)]
                print(seq)
            sequences.append(SeqRecord.SeqRecord(Seq.Seq(seq), id=str(i+1),description=""))

        SeqIO.write(sequences, "random.fasta", "fasta")



from Bio import SeqIO

READS = [str(r.seq) 
        for r in list(SeqIO.read('../generateReads/simReads.fa', 'fasta'))
        ]


def check_answer(assembled_sequence):
    pass

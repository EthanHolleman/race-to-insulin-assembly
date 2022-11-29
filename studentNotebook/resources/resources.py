from Bio import SeqIO
from Bio import pairwise2

INSULIN_FA = '../generateReads/insulinSeq.fasta'
INSULIN_REC = SeqIO.read(INSULIN_FA, 'fasta')
READS = [str(r.seq)
        for r in list(SeqIO.parse('../generateReads/simReads.fa', 'fasta'))
        ]


def check_answer(assembled_sequence, score_only=True):
        '''Calculate global alignment between assembled_sequence
        and true answer to determine score for the answer.
        '''
        if not isinstance(assembled_sequence, str):
                print('Your assembled sequence must be passed as a string!')
                return

        # 1 point for correct base, -1 for incorrect, -0.5 for gap
        # opening and -0.5 for gap extension.
        alignment = pairwise2.align.globalms(
        assembled_sequence.upper(), str(INSULIN_REC.seq),
        1, -1, -.5, -.5
        )[0]
        if alignment.score == len(INSULIN_REC):
                print('PERFECT SCORE!!!!!!!! CONGRATS!!!!!!')
        print('Alignment score:', alignment.score)
        if not score_only:
                print(alignment[0])
        return alignment.score

    

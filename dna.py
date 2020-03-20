def elementarycomplement(string, base, comp_base, swap='x'): 
    ''' Elementary swap of bases
    '''
    return string.replace(base,swap).replace(comp_base,base).replace(swap, comp_base)

class DNAseq:
    '''Class to include DNA sequence with methods
    Input:
       - DNA string with sequence
    '''
    def __init__(self, seq):
        self.seq = seq
        self.length = len(seq)
        
    def toRNA(self):
        ''' Transform a DNA string to an equivalent RNA string, by tranforming
        all the thymine bases to uracil, irrespective or whether they are
        capital or small letters.
        '''

        return self.seq.replace('T','U').replace('t','u')
    

    def reversecomplement(self):
        '''Transform a DNA string to its reverse complement.
        '''
        complement = self.seq[::-1]
        complement = elementarycomplement(complement,'A','T')
        complement = elementarycomplement(complement,'G','C')
        complement = elementarycomplement(complement,'a','t')
        complement = elementarycomplement(complement,'g','c')
        self.rev_comp = complement
        return complement
    
    def countbases(self, bases = ['A', 'C', 'G', 'T']):
        '''Count number of times each base appears.
        '''
        counts = [self.seq.count(base) for base in bases]
        self.counts = counts
        
        return counts
    
    def __len__(self):
        return self.length
    
    def __str__(self):
        return self.seq
    
    def __add__(self, dna_seq2):
        return DNAseq(self.seq+dna_seq2.seq)
    

# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: YOUR NAME HERE
"""

# you may find it useful to import these variables (although you are not required to use them)
from amino_acids import aa, codons, AminoAcids, Nucleotides

def collapse(L):
    """ Converts a list of strings to a string by concatenating all elements of the list """
    output = ""
    for s in L:
        output = output + s
    return output


def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment
    """
    Amino=[]
    codon=''
    AminoA=[]
    for i in range(len(dna)/3):
        if i==0:
            codon=(dna[(0):(3)])
            Amino.append(codon)
            codon=''
        else:
            codon=(dna[(i*3):((1+i)*3)])
            Amino.append(codon)
            codon=''
    for x in range(len(Amino)):
        AminoA+=[Nucleotides[Amino[x]]]
    return AminoA
            
                
                
        

def coding_strand_to_AA_unit_tests():
    """ Unit tests for the coding_strand_to_AA function """
        
    # YOUR IMPLEMENTATION HERE

def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    """
    rdna=''
    for i in range(len(dna)):
        if dna[i]=='A':
            rdna+='T'
        if dna[i]=='T':
            rdna+='A'
        if dna[i]=='C':
            rdna+='G'
        if dna[i]=='G':
            rdna+='C'
    return rdna
    
def get_reverse_complement_unit_tests():
    """ Unit tests for the get_complement function """
        
    # YOUR IMPLEMENTATION HERE    

def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.
        
        dna: a DNA sequence
        returns: the open reading frame represented as a string
    """
    
    

def rest_of_ORF_unit_tests():
    """ Unit tests for the rest_of_ORF function """
        
    # YOUR IMPLEMENTATION HERE
        
def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
     
#<<<<<<< HEAD
    Amino=[]
    codon=''
    AminoA=[]
    for i in range(len(dna)/3):
        if i==0:
            codon=(dna[(0):(3)])
            Amino.append(codon)
            codon=''
        else:
            codon=(dna[(i*3):((1+i)*3)])
            Amino.append(codon)
            codon=''
    for x in range(len(Amino)):
        AminoA+=[Nucleotides[Amino[x]]]
    return AminoA    
        
#=======
    # YOUR IMPLEMENTATION HERE        
     
def find_all_ORFs_oneframe_unit_tests():
    """ Unit tests for the find_all_ORFs_oneframe function """

    # YOUR IMPLEMENTATION HERE

#>>>>>>> upstream/master
def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    ORFs=[]
    ORF=[]
    codon=''
    i=0
    while i<(len(dna)/3):
        if i==0:
            codon=(dna[(0):(3)])
            i+=1
            if codon=='ATG':
                for y in range(i-1,len(dna)):
                    codon=(dna[(y*3):((y+1)*3)])
                    
                    if codon=='TAA' or codon=='TAG' or codon=='TGA':
                        codon=''
                        ORFs+=[ORF]
                        ORF=[]
                        break
                    else:
                        ORF.append(codon)
                        codon=''
                        i+=1
        else:
            codon=(dna[(i*3):((1+i)*3)])
            i+=1
            if codon=='ATG':
                for y in range(i-1,len(dna)):
                    codon=(dna[(y*3):((y+1)*3)])
                    
                    if codon=='TAA' or codon=='TAG' or codon=='TGA':
                        codon=''
                        ORFs+=[ORF]
                        ORF=[]
                        break
                    else:
                        ORF.append(codon)
                        codon=''
                        i+=1
                        
    return ORFs
    
def find_all_ORFs_unit_tests():
    """ Unit tests for the find_all_ORFs function """
        
    # YOUR IMPLEMENTATION HERE

def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
     
    # YOUR IMPLEMENTATION HERE

def find_all_ORFs_both_strands_unit_tests():
    """ Unit tests for the find_all_ORFs_both_strands function """

    # YOUR IMPLEMENTATION HERE

def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string"""
    longer1=[]
    ORF=find_all_ORFs(dna)
    for i in range(len(ORF)-1):
        longer=longer1
        if len(ORF[i])>len(ORF[i+1]):
            longer1=ORF[i]
        elif len(ORF[i])<=len(ORF[i+1]):
            longer1=ORF[i+1]  
        if len(longer)>=len(longer1):
            longer1=longer
        else:
            longer=longer1
    return longer

def longest_ORF_unit_tests():
    """ Unit tests for the longest_ORF function """

    # YOUR IMPLEMENTATION HERE

def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """

    # YOUR IMPLEMENTATION HERE

def gene_finder(dna, threshold):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.
        
        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid
                   gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum
                 length specified.
    """

    # YOUR IMPLEMENTATION HERE
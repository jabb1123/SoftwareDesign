# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: YOUR NAME HERE
"""

# you may find it useful to import these variables (although you are not required to use them)
from amino_acids import aa, codons, AminoAcids, Nucleotides
from random import shuffle

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
    AminoA=''
    for i in range(len(dna)/3):
        codon=(dna[(i*3):(i*3+3)])
        Amino.append(codon)
        codon=''
    for x in range(len(Amino)):
        AminoA+=Nucleotides[Amino[x]]
    return AminoA
            
                
                
        

def coding_strand_to_AA_unit_tests():
    """ Unit tests for the coding_strand_to_AA function """
        
    x = "ATG"
    xo = "M"
    y = "CAGCGTTGGATGCAA"
    yo = "QRWMQ"
    z = "ATAATGTGTAATCA"
    zo = "IMCN"
    print "input: " + x + ", expected output: " + xo + ", actual output: " + coding_strand_to_AA(x)
    print "input: " + y + ", expected output: " + yo + ", actual output: " + coding_strand_to_AA(y)
    print "input: " + z + ", expected output: " + zo + ", actual output: " + coding_strand_to_AA(z)

def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    """
    rdna=''
    mdna=''
    for i in range(len(dna)):
        if dna[i]=='A':
            mdna+='T'
        if dna[i]=='T':
            mdna+='A'
        if dna[i]=='C':
            mdna+='G'
        if dna[i]=='G':
            mdna+='C'
    for x in range(1,len(mdna)+1):
        rdna+=mdna[-x]
    return rdna
    
def get_reverse_complement_unit_tests():
    """ Unit tests for the get_complement function """
        
    x = "AAA" 
    xo = "TTT"
    y = "CAGCGTTGGATGCAA"
    yo = "TTGCATCCAACGCTG"
    z = "ATAATGTGTAATCA"
    zo = "TGATTACACATTAT"
    print "input: " + x + ", expected output: " + xo + ", actual output: " + get_reverse_complement(x)
    print "input: " + y + ", expected output: " + yo + ", actual output: " + get_reverse_complement(y)
    print "input: " + z + ", expected output: " + zo + ", actual output: " + get_reverse_complement(z)    

def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.
        
        dna: a DNA sequence
        returns: the open reading frame represented as a string
    """
    Amino=''
    codon=''
    stopCodon=codons[10]
    for i in range(len(dna)/3):
        codon=(dna[(i*3):(i*3+3)])
        if codon!=stopCodon[0] and codon!=stopCodon[1] and codon!=stopCodon[2]:
            Amino+=codon
            codon=''
        elif codon==stopCodon[0] or codon==stopCodon[1] or codon==stopCodon[2]:
            return Amino
            Amino=''
            break
    return Amino
    

def rest_of_ORF_unit_tests():
    """ Unit tests for the rest_of_ORF function """
        
    x = "ATG"
    xo = "ATG"
    y = "ATGTTTTGATGAA"
    yo = "ATGTTT"
    z = "ATGATGTGTAGATCA"
    zo = "ATGATGTGTAGATCA"
    print "input: " + x + ", expected output: " + xo + ", actual output: " + rest_of_ORF(x)
    print "input: " + y + ", expected output: " + yo + ", actual output: " + rest_of_ORF(y)
    print "input: " + z + ", expected output: " + zo + ", actual output: " + rest_of_ORF(z)
        
def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    Amino=[]
    i=0
    while i<=len(dna):
        codon=(dna[(i*3):(i*3+3)])
        if codon=='ATG':
            ndna=dna[i*3:len(dna)]
            rna=rest_of_ORF(ndna)
            Amino.append(rna)
            i+=len(rna)/3
        i+=1
    return Amino

def find_all_ORFs_oneframe_unit_tests():
    """ Unit tests for the find_all_ORFs_oneframe function """

    x = "ATGGGGGGGTGA"
    xo = "[ATGGGGGGG]"
    y = "ATGTTTTAAATGAAATAG"
    yo = "[ATGTTT,ATGAAA]"
    z = "ATGGGGTAGGGGATGCCCTAA"    
    zo = "[ATGGGG,ATGCCC]"
    print "input: " + x + ", expected output: " + xo + ", actual output: " + str(find_all_ORFs_oneframe(x))
    print "input: " + y + ", expected output: " + yo + ", actual output: " + str(find_all_ORFs_oneframe(y))
    print "input: " + z + ", expected output: " + zo + ", actual output: " + str(find_all_ORFs_oneframe(z))
    
def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    rna=dna[1:len(dna)]
    tna=dna[2:len(dna)]
    first_frame=find_all_ORFs_oneframe(dna)
    second_frame=find_all_ORFs_oneframe(rna)
    third_frame=find_all_ORFs_oneframe(tna)
    return first_frame , second_frame , third_frame
    
    
    
def find_all_ORFs_unit_tests():
    """ Unit tests for the find_all_ORFs function """
        
    x = "ATGGATGGTGAATGAGTGA"
    xo = "[ATGGATGGTGA,ATGGTGAATGAG,ATGAGTGA]"
    y = "ATGTTTTAATGAAATAG"
    yo = "[ATGTTT,ATGAAA]"
    z = "ATGGGGTAGTGAGGTATGAGCTACCTATGAA"
    zo = "[ATGGGG,ATGAGCTACCTA,ATGAA]"
    print "input: " + x + ", expected output: " + xo + ", actual output: " + str(find_all_ORFs(x))
    print "input: " + y + ", expected output: " + yo + ", actual output: " + str(find_all_ORFs(y))
    print "input: " + z + ", expected output: " + zo + ", actual output: " + str(find_all_ORFs(z))  

def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    rna=get_reverse_complement(dna)
    strand=find_all_ORFs(dna)
    reverse=find_all_ORFs(rna)
    return(strand, reverse)

def find_all_ORFs_both_strands_unit_tests():
    """ Unit tests for the find_all_ORFs_both_strands function """

    x = "ATGGATGGTGAATGAGTGA"
    xo = "[ATGGATGGTGA,ATGGTGAATGAG,ATGAGTGA]"
    y = "ATGTTTTAATGAAATAG"
    yo = "[ATGTTT, ATGAAA]"
    z = "ATGGGGTAGTGAGGTATGAGCTACCTATGAA"
    zo = "[ATGGGG,ATGAGCTACCTA,ATGAA]"
    print "input: " + x + ", expected output: " + xo + ", actual output: " + str(find_all_ORFs_both_strands(x))
    print "input: " + y + ", expected output: " + yo + ", actual output: " + str(find_all_ORFs_both_strands(y))
    print "input: " + z + ", expected output: " + zo + ", actual output: " + str(find_all_ORFs_both_strands(z))

def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string"""
    t=find_all_ORFs_both_strands(dna)  
    x=t[0] 
    h=x[0]
    if not h:
        longest=''
    else:    
        longest=h[0]
    for y in range(len(t)):
        temp=t[y]
        for z in range(len(temp)):
            temp2=temp[z]
            for i in range(len(temp2)):
                if (len(temp2[i]))>len(longest):
                    longest=temp2[i]
    return longest

def longest_ORF_unit_tests():
    """ Unit tests for the longest_ORF function """

    x = "ATGGATGGTGAATGAGTGA" 
    xo = "ATGGATGGTGAA"
    y = "ATGTTTTAATGAAATAG"
    yo = "ATGTTT"
    z = "ATGGGGTAGTGAGGTATGAGCTACCTATGAA"
    zo = "ATGAGCTACCTA"
    print "input: " + x + ", expected output: " + xo + ", actual output: " + longest_ORF(x)
    print "input: " + y + ", expected output: " + yo + ", actual output: " + longest_ORF(y)
    print "input: " + z + ", expected output: " + zo + ", actual output: " + longest_ORF(z)

def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """
    code=[]
    x=0
    longer=0
    while x<num_trials:
        for i in range(len(dna)):
            code+=[dna[i]]
        shuffle(code)
        ndna=collapse(code)
        code=[]
        lon=longest_ORF(ndna)
        x+=1
        if longer< len(lon):
            longer=len(lon)
    return longer
    

def gene_finder(dna, threshold):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.
        
        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid
                   gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum
                 length specified.
    """
    AAS=[]
    t=find_all_ORFs_both_strands(dna)
    for y in range(len(t)):
        temp=t[y]
        for z in range(len(temp)):
            temp2=temp[z]
            for i in range(len(temp2)):
                if (len(temp2[i]))>threshold:
                    code=temp2[i]
                    AAS+=[coding_strand_to_AA(code)]
    return AAS
                    
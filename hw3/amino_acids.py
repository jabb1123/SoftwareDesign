aa = ['F','L','I','M','V','S','P','T','A','Y',
      '|','H','Q','N','K','D','E','C','W','R',
      'G']

codons = [['TTT', 'TTC'],
          ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
          ['ATT', 'ATC', 'ATA'],
          ['ATG'],
          ['GTT', 'GTC', 'GTA', 'GTG'],
          ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],
          ['CCT', 'CCC', 'CCA', 'CCG'],
          ['ACT', 'ACC', 'ACA', 'ACG'],
          ['GCT', 'GCC', 'GCA', 'GCG'],
          ['TAT', 'TAC'],
          ['TAA', 'TAG', 'TGA'],
          ['CAT', 'CAC'],
          ['CAA', 'CAG'],
          ['AAT', 'AAC'],
          ['AAA', 'AAG'],
          ['GAT', 'GAC'],
          ['GAA', 'GAG'],
          ['TGT', 'TGC'],
          ['TGG'],
          ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
          ['GGT', 'GGC', 'GGA', 'GGG']]
              
AminoAcids={'F':'TTT', 'F':'TTC', 'L':'TTA', 'L':'TTG', 'L':'CTT', 'L':'CTC',
            'L':'CTA', 'L':'CTG', 'I':'ATT', 'I':'ATC', 'I':'ATA', 'M':'ATG',
            'V':'GTT', 'V':'GTC', 'V':'GTA', 'V':'GTG', 'S':'TCT', 'S':'TCC',
            'S':'TCA', 'S':'TCG', 'S':'AGT', 'S':'AGC', 'P':'CCT', 'P':'CCC',
            'P':'CCA', 'P':'CCG', 'T':'ACT', 'T':'ACC', 'T':'ACA', 'T':'ACG',
            'A':'GCT', 'A':'GCC', 'A':'GCA', 'A':'GCG', 'Y':'TAT', 'Y':'TAC',
            '|':'TAA', '|':'TAG', '|':'TGA', 'H':'CAT', 'H':'CAC', 'Q':'CAA',
            'Q':'CAG', 'N':'AAT', 'N':'AAC', 'K':'AAA', 'K':'AAG', 'D':'GAT',
            'D':'GAC', 'E':'GAA', 'E':'GAG', 'C':'TGT', 'C':'TCG', 'W':'TGG',
            'R':'CGT', 'R':'CGC', 'R':'CGA', 'R':'CGG', 'R':'AGA', 'R':'AGG',
            'G':'GGT', 'G':'GGC', 'G':'GGA', 'G':'GGG'}

Nucleotides={}
for i in range(len(codons)):
    ind=codons[i]
    for x in range(len(ind)):
        codon=ind[x]
        Nucleotides.update({ind[x]:aa[i]})
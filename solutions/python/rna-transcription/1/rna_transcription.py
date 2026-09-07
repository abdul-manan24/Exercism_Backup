def to_rna(dna_strand):
    RNA = ''
    for nucleotides in dna_strand:
        match nucleotides:
            case 'G':
                RNA += 'C'
            case 'C':
                RNA += 'G'
            case 'T':
                RNA += 'A'
            case 'A':
                RNA += 'U'
            case _:
                continue

    return RNA

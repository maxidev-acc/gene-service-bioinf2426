


valid_nucleotides = ["A", "T", "G", "C"]

def verify_input_dna_sequence(input_sequence):
    for nuc in input_sequence.upper():
        if nuc not in valid_nucleotides:
            return False, f"Invalid Nucleotide: {nuc}. Allowed nucleotides are {', '.join(valid_nucleotides)}"
    return True, "Valid sequence"
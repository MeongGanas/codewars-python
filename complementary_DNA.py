def DNA_strand(dna):
    # code here
    key = {"T": "A", "A": "T", "C": "G", "G": "C"}
    return ''.join([key[i] for i in dna])


print(DNA_strand("ATTGC"))

def rna_transcription(dna):
    rnaStr = ""
    for letter in dna:
        if letter == "G":
            rnaStr += "C"
        
        elif letter == "C":
            rnaStr += "G"

        elif letter == "T":
            rnaStr += "A"
        
        elif letter == "A":
            rnaStr += "U"

    return rnaStr

def main():
    dna = input("Enter an DNA strand (letters: G-C-T-A)...")

    print(f"DNA: {dna}\tRNA: {rna_transcription(dna)}")

if __name__ == "__main__":
    main()
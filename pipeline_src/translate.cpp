#include <iostream>
#include <unordered_map>
#include <string>
#include <cstdlib>

// Function to translate codon to amino acid
std::string translate_codon(const std::string& codon) {
    // Define the codon to amino acid mapping (simplified)
    std::unordered_map<std::string, char> codon_table = {
        {"TTT", 'F'}, {"TTC", 'F'}, {"TTA", 'L'}, {"TTG", 'L'},
        {"CTT", 'L'}, {"CTC", 'L'}, {"CTA", 'L'}, {"CTG", 'L'},
        {"ATT", 'I'}, {"ATC", 'I'}, {"ATA", 'I'}, {"ATG", 'M'},
        {"GTT", 'V'}, {"GTC", 'V'}, {"GTA", 'V'}, {"GTG", 'V'},
        {"TCT", 'S'}, {"TCC", 'S'}, {"TCA", 'S'}, {"TCG", 'S'},
        {"CCT", 'P'}, {"CCC", 'P'}, {"CCA", 'P'}, {"CCG", 'P'},
        {"ACT", 'T'}, {"ACC", 'T'}, {"ACA", 'T'}, {"ACG", 'T'},
        {"GCT", 'A'}, {"GCC", 'A'}, {"GCA", 'A'}, {"GCG", 'A'},
        {"TAT", 'Y'}, {"TAC", 'Y'}, {"TAA", '*'}, {"TAG", '*'},
        {"CAT", 'H'}, {"CAC", 'H'}, {"CAA", 'Q'}, {"CAG", 'Q'},
        {"AAT", 'N'}, {"AAC", 'N'}, {"AAA", 'K'}, {"AAG", 'K'},
        {"GAT", 'D'}, {"GAC", 'D'}, {"GAA", 'E'}, {"GAG", 'E'},
        {"TGT", 'C'}, {"TGC", 'C'}, {"TGA", '*'}, {"TGG", 'W'},
        {"CGT", 'R'}, {"CGC", 'R'}, {"CGA", 'R'}, {"CGG", 'R'},
        {"AGT", 'S'}, {"AGC", 'S'}, {"AGA", 'R'}, {"AGG", 'R'},
        {"GGT", 'G'}, {"GGC", 'G'}, {"GGA", 'G'}, {"GGG", 'G'}
    };

    auto it = codon_table.find(codon);
    if (it != codon_table.end()) {
        return std::string(1, it->second);
    }
    return "";
}

// Function to translate DNA sequence to protein sequence
std::string translate_dna_to_protein(const std::string& dna) {
    std::string protein = "";
    // Ensure the DNA sequence length is a multiple of 3
    for (size_t i = 0; i < dna.length(); i += 3) {
        if (i + 2 < dna.length()) {
            std::string codon = dna.substr(i, 3);
            std::string aminoAcid = translate_codon(codon);
            if (aminoAcid != "*") {
                protein += aminoAcid;
            } else {
                break;  // Stop at stocodon
            }
        }
    }
    return protein;
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <DNA_sequence>" << std::endl;
        return 1;
    }

    std::string dna_sequence = argv[1];
    std::string protein_sequence = translate_dna_to_protein(dna_sequence);
    std::cout << protein_sequence << std::endl;
    return 0;
}
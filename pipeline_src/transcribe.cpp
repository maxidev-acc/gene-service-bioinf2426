#include <iostream>
#include <string>
#include <cstdlib>

// Function to transcribe DNA to RNA
std::string transcribe_dna_to_rna(const std::string& dna) {
    std::string rna = dna;
    for (char& base : rna) {
        if (base == 'T') {
            base = 'U';
        }
    }
    return rna;
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <DNA_sequence>" << std::endl;
        return 1;
    }

    std::string dna_sequence = argv[1];
    std::string rna_sequence = transcribe_dna_to_rna(dna_sequence);

    std::cout << rna_sequence << std::endl;
    return 0;
}
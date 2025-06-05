from fastapi import APIRouter, Request, HTTPException, Depends
from utils.verify_dna_seq import verify_input_dna_sequence
import subprocess
from config import config


gene_router= APIRouter(
    prefix="/genex",
    tags=["gene-expression"],
)


@gene_router.get("/translate/{dna_sequence}")
def translate_dna_to_protein(dna_sequence: str):
    """
    Translates a DNA sequence into a protein sequence by reversing the input sequence.
    
    """



    is_valid, message = verify_input_dna_sequence(dna_sequence)
    if not is_valid:
        raise HTTPException(status_code=400, detail=message)

    result = subprocess.run(
        [config["TRANSLATION_SERVICE_PATH"], dna_sequence],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        raise HTTPException(status_code=500, detail="Translation service failed")
    
    protein_sequence = result.stdout.strip()

    return {"msg": "Translation worked succesfully", "protein_sequence": protein_sequence}


@gene_router.get("/transcribe/{dna_sequence}")
def transcribe_dna_to_rna(dna_sequence: str):
    """
    Transcribes a DNA sequence into an RNA sequence by reversing the input sequence."""

    is_valid, message = verify_input_dna_sequence(dna_sequence)
    if not is_valid:
        raise HTTPException(status_code=400, detail=message)

    result = subprocess.run(
        [config["TRANSCRIPTION_SERVICE_PATH"], dna_sequence],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        raise HTTPException(status_code=500, detail="Translation service failed")
    
    rna_sequence = result.stdout.strip()

    return {"msg": "Transcription worked succesfully", "dna_sequence": dna_sequence, "rna_sequence": rna_sequence}
import os
from src.input_parser import load_fasta, load_yaml

def main():
    fasta_path = os.path.join("inputs", "antigen.fasta")
    yaml_path = os.path.join("inputs", "config.yaml")

    protein_id, sequence = load_fasta(fasta_path)
    config = load_yaml(yaml_path)

    print(f"Loaded antigen: {protein_id}")
    print(f"Sequence (first 50 aa): {sequence[:50]}...")
    print(f"Config: {config}")

if __name__ == "__main__":
    main()

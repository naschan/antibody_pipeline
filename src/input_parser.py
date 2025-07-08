from Bio import SeqIO
import yaml

def load_fasta(file_path):
    record = SeqIO.read(file_path, "fasta")
    return record.id, str(record.seq)

def load_yaml(file_path):
    with open(file_path, 'r') as f:
        config = yaml.safe_load(f)
    return config

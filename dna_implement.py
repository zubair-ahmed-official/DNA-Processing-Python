"""
9.1PP Divide and Conquer - DNA Implementation
"""
__author__ = "ZUBAIR AHMED" 

# Processing Module
def clean_sequence(sequence: str) -> str:
    """Cleans the given DNA sequence by replacing invalid bases with """
    valid_bases = {'A', 'T', 'G', 'C'}
    return ''.join(base if base in valid_bases else '.' for base in sequence.upper())

def calculate_error_rate(sequence: str) -> float:
    """ Calculates the error rate of the cleaned DNA sequence. """
    errors = sequence.count('.')
    return round((errors / len(sequence)) * 100, 1)

def generate_complement(sequence: str) -> str:
    """ Generates the complement of the given DNA sequence. """
    complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G', '.': '.'}
    return ''.join(complement[base] for base in sequence)

def transcribe_sequence(sequence: str) -> str:
    """ Transcribes the given DNA sequence to mRNA by replacing 'T' with 'U'. """
    return sequence.replace('T', 'U')

def transcribe_section(sequence: str, start: int, length: int) -> str:
    """ Transcribes a specified section of the given DNA sequence to mRNA. """
    section = sequence[start-1:start-1+length]
    return transcribe_sequence(section)

def splice_sequence(original: str, addition: str) -> str:
    """ Splices an additional DNA sequence into the original sequence after cleaning it. """ 
    return original + clean_sequence(addition)
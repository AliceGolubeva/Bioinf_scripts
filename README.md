# Bioinf_scripts

Bioinf_scripts is a lightweight Python toolkit for processing and analyzing common bioinformatics file formats, including FASTQ, FASTA, and BLAST output. It is designed to be memory-efficient, processing large files "on the fly" (streaming) without loading entire datasets into RAM.

**Author:**  
Alice Golubeva,  
Institute of Bioinformatics, Russia.

---

## Content
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Running Instructions](#running-instructions)
- [Examples](#examples)
- [Contact](#contact)
- [License](#license)

---

## Installation

To run Bioinf_scripts, you only need **Python 3.9 or higher**. The toolkit is built exclusively using the Python standard library, so no external dependencies (like Biopython) are required.

You can clone the repository directly from GitHub:

```bash
git clone https://github.com/AliceGolubeva/Bioinf_scripts.git
cd Bioinf_scripts
```

---

## Project Structure

```text
Bioinf_scripts/
├── bioinf_scripts.py       # Main entry point and utility functions
├── helpers/
│   ├── __init__.py
│   ├── fastq.py            # Helper functions for FASTQ processing
│   └── bio_files.py        # Helper functions for FASTA and BLAST parsing
└── README.md
```

---

## Running Instructions

To use the toolkit, import the required functions directly into your Python scripts or Jupyter Notebook. 

The package provides three main utilities:
1. `filter_fastq`: Filters FASTQ reads by GC content, length, and average quality.
2. `convert_multiline_fasta_to_oneline`: Converts multiline FASTA sequences into a single-line format.
3. `parse_blast_output`: Extracts the best hit description from a standard BLAST text output.

To view detailed documentation for any function, use Python's built-in `help()` function:
```python
from bioinf_scripts import filter_fastq
help(filter_fastq)
```

---

## Examples

### 1. FASTQ Filtering
Filter reads to keep only those with GC content between 40% and 60%, length between 100 and 300 bp, and an average Phred33 quality score of at least 30.

```python
from bioinf_scripts import filter_fastq

filter_fastq(
    input_fastq="raw_reads.fastq",
    output_fastq="clean_reads.fastq",
    gc_bounds=(40, 60),           # Tuple: (min_GC, max_GC)
    length_bounds=(100, 300),     # Tuple: (min_length, max_length)
    quality_threshold=30          # Minimum average quality
)
```
*Note: Filtered reads are automatically saved into a newly created `filtered/` directory.*

### 2. FASTA Multiline to Oneline Conversion
Convert a FASTA file where sequences are split across multiple lines into a standard single-line format. If the output filename is not provided, it will be generated automatically with an `_oneline` suffix.

```python
from bioinf_scripts import convert_multiline_fasta_to_oneline

# Explicit output name
convert_multiline_fasta_to_oneline("input.fasta", "output.fasta")

# Automatic output name (creates "input_oneline.fasta")
convert_multiline_fasta_to_oneline("input.fasta")
```

### 3. BLAST Output Parsing
Extract the description of the best alignment hit for each query from a standard BLAST text output and save them as a sorted list.

```python
from bioinf_scripts import parse_blast_output

parse_blast_output(
    input_file="blast_results.txt", 
    output_file="best_hits_sorted.txt"
)
```

---

## Contact

For questions, suggestions, or bug reports, please open an issue on the GitHub repository or contact the author via GitHub: [@AliceGolubeva](https://github.com/AliceGolubeva).

---

## License

This project is developed for educational and research purposes. 
Copyright (c) 2026 Alice Golubeva.

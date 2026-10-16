import os
from helpers.bio_files import read_fasta, write_fasta


def convert_multiline_fasta_to_oneline(
    input_fasta: str,
    output_fasta: str | None = None
) -> str:
    """
    Конвертирует multiline FASTA файл в oneline формат.
    Каждая последовательность умещается в одну строку.

    Arguments:
        input_fasta: путь до входного FASTA файла
        output_fasta: путь до выходного файла. Если не указан,
                      создаётся файл с суффиксом '_oneline' в той же папке.

    Returns:
        str: путь до созданного выходного файла
    """
    
    if output_fasta is None:
        base, ext = os.path.splitext(input_fasta)
        output_fasta = f"{base}_oneline{ext}"

   
    if os.path.exists(output_fasta):
        os.remove(output_fasta)

   
    for header, sequence in read_fasta(input_fasta):
        write_fasta(output_fasta, header, sequence)

    return output_fasta



from helpers.bio_files import parse_blast_queries, write_sorted_list


def parse_blast_output(input_file: str, output_file: str) -> None:
    """
    Парсит BLAST output и извлекает описание лучшего хита для каждого QUERY.
    Результаты сохраняются в выходной файл одним столбцом, отсортированные по алфавиту.

    Arguments:
        input_file: путь до входного BLAST output файла (txt)
        output_file: путь до выходного файла с описаниями белков
    """
    best_hits = parse_blast_queries(input_file)
    write_sorted_list(output_file, best_hits)

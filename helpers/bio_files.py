from typing import Iterator, Tuple


def read_fasta(file_path: str) -> Iterator[Tuple[str, str]]:
    """
    Читает FASTA файл и возвращает кортежи (header, sequence) по одному за раз.
    Последовательность собирается из нескольких строк в одну.

    Arguments:
        file_path: путь до FASTA файла

    Yields:
        Tuple[str, str]: (header, sequence)
    """
    header = None
    sequence_parts = []

    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith('>'):
                # Если уже есть предыдущая запись — отдаём её
                if header is not None:
                    yield header, ''.join(sequence_parts)
                header = line
                sequence_parts = []
            else:
                sequence_parts.append(line)
 
    if header is not None:
        yield header, ''.join(sequence_parts)


def write_fasta(file_path: str, header: str, sequence: str) -> None:
    """
    Записывает одну FASTA запись в файл.

    Arguments:
        file_path: путь до файла
        header: заголовок (включая '>')
        sequence: последовательность одной строкой
    """
    with open(file_path, 'a') as f:
        f.write(f"{header}\n{sequence}\n")


from typing import List


def extract_best_hit_description(line: str) -> str:
    """
    Извлекает описание лучшего хита из строки BLAST output.
    Описание находится до первого числового значения (Score).

    Arguments:
        line: строка из BLAST output с описанием хита

    Returns:
        str: описание белка, очищенное от лишних пробелов
    """
    parts = line.split()
    description_parts = []
    for part in parts:
        try:
            float(part)
            break
        except ValueError:
            description_parts.append(part)
    return ' '.join(description_parts).strip()


def parse_blast_queries(file_path: str) -> List[str]:
    """
    Парсит BLAST output и извлекает описание лучшего хита для каждого QUERY.

    Arguments:
        file_path: путь до BLAST output файла

    Returns:
        List[str]: список описаний лучших хитов (без дубликатов)
    """
    best_hits: List[str] = []
    marker = "Sequences producing significant alignments:"

    with open(file_path, 'r') as f:
        lines = f.readlines()

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        if marker in line:
            i += 1
            while i < len(lines) and 'Description' in lines[i]:
                i += 1
            while i < len(lines) and not lines[i].strip():
                i += 1

            if i < len(lines):
                best_hit_line = lines[i].strip()
                if best_hit_line:
                    description = extract_best_hit_description(best_hit_line)
                    if description:
                        best_hits.append(description)
        i += 1

    return best_hits


def write_sorted_list(file_path: str, items: List[str]) -> None:
    """
    Записывает список строк в файл, отсортированный по алфавиту.

    Arguments:
        file_path: путь до выходного файла
        items: список строк для записи
    """
    with open(file_path, 'w') as f:
        for item in sorted(items):
            f.write(f"{item}\n")

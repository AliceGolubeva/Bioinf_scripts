# helpers/bio_files.py
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

    # Не забываем отдать последнюю запись
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
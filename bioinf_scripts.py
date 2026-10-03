# bioinf_scripts.py
import os
from helpers.fastq import (
    read_fastq,
    write_fastq,
    check_gc_bounds,
    check_length_bounds,
    check_quality_threshold
)


def filter_fastq(input_fastq, output_fastq, gc_bounds=(0, 100), 
                 length_bounds=(0, 2**32), quality_threshold=0):
    """
    Фильтрует FASTQ файл по заданным критериям.
    
    Args:
        input_fastq: путь до входного FASTQ файла
        output_fastq: имя выходного файла (сохраняется в папку filtered/)
        gc_bounds: интервал GC состава (по умолчанию (0, 100))
        length_bounds: интервал длины (по умолчанию (0, 2**32))
        quality_threshold: порог среднего качества (по умолчанию 0)
    """
    # Создаем папку filtered/, если её нет
    output_dir = "filtered"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Полный путь к выходному файлу
    output_path = os.path.join(output_dir, output_fastq)
    
    # Очищаем выходной файл, если он существует
    if os.path.exists(output_path):
        os.remove(output_path)
    
    # Читаем и фильтруем "на лету"
    for header, sequence, quality in read_fastq(input_fastq):
        # Проверяем все критерии
        passes_gc = check_gc_bounds(sequence, gc_bounds)
        passes_length = check_length_bounds(sequence, length_bounds)
        passes_quality = check_quality_threshold(quality, quality_threshold)
        
        # Если рид проходит все фильтры - записываем его
        if passes_gc and passes_length and passes_quality:
            write_fastq(output_path, header, sequence, quality)


# Пример использования
if __name__ == "__main__":
    # Пример вызова функции
    filter_fastq(
        input_fastq="example.fastq",
        output_fastq="filtered_output.fastq",
        gc_bounds=(20, 80),
        length_bounds=(50, 300),
        quality_threshold=20
    )
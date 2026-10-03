# helpers/fastq.py

def read_fastq(file_path):
    """
    Генератор, который читает FASTQ файл по одному риду за раз.
    Возвращает кортеж: (header, sequence, quality_string)
    """
    with open(file_path, 'r') as f:
        while True:
            header = f.readline().strip()
            if not header:
                break
            sequence = f.readline().strip()
            plus = f.readline().strip()
            quality = f.readline().strip()
            yield header, sequence, quality


def write_fastq(file_path, header, sequence, quality):
    """
    Записывает один рид в FASTQ файл.
    """
    with open(file_path, 'a') as f:
        f.write(f"{header}\n{sequence}\n+\n{quality}\n")


def calculate_gc_content(sequence):
    """
    Рассчитывает GC состав последовательности в процентах.
    Возвращает float от 0 до 100.
    """
    if not sequence:
        return 0.0
    gc_count = sequence.upper().count('G') + sequence.upper().count('C')
    return (gc_count / len(sequence)) * 100


def check_gc_bounds(sequence, gc_bounds):
    """
    Проверяет, попадает ли GC состав в заданные границы.
    gc_bounds может быть числом (верхняя граница) или кортежем (min, max).
    Возвращает True, если проходит фильтр.
    """
    gc_content = calculate_gc_content(sequence)
    
    # Если передано одно число - это верхняя граница
    if isinstance(gc_bounds, (int, float)):
        return gc_content <= gc_bounds
    
    # Если передан кортеж - проверяем диапазон
    min_gc, max_gc = gc_bounds
    return min_gc <= gc_content <= max_gc


def check_length_bounds(sequence, length_bounds):
    """
    Проверяет, попадает ли длина последовательности в заданные границы.
    length_bounds может быть числом (верхняя граница) или кортежем (min, max).
    Возвращает True, если проходит фильтр.
    """
    seq_length = len(sequence)
    
    # Если передано одно число - это верхняя граница
    if isinstance(length_bounds, (int, float)):
        return seq_length <= length_bounds
    
    # Если передан кортеж - проверяем диапазон
    min_len, max_len = length_bounds
    return min_len <= seq_length <= max_len


def calculate_average_quality(quality_string):
    """
    Рассчитывает среднее качество рида по строке качества (phred33).
    Возвращает float.
    """
    if not quality_string:
        return 0.0
    total_quality = sum(ord(char) - 33 for char in quality_string)
    return total_quality / len(quality_string)


def check_quality_threshold(quality_string, quality_threshold):
    """
    Проверяет, превышает ли среднее качество пороговое значение.
    Возвращает True, если проходит фильтр.
    """
    avg_quality = calculate_average_quality(quality_string)
    return avg_quality >= quality_threshold
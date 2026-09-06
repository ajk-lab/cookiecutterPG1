def compare_counts(source_count, target_count):
    return {
        "source_count": source_count,
        "target_count": target_count,
        "matched": source_count == target_count
    }

def make_table(column):
    return column.value_counts().sort_index()
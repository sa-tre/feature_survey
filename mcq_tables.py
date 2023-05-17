def make_table(column):
    """Converts to percentages and makes md table"""
    table_dict = column.value_counts().sort_index().to_dict()
    total = sum(table_dict.values())
    for k, v in table_dict.items():
        perc = round(v / total * 100, 2)
        table_dict[k] = '%.2f' % perc + "%"
    return table_dict

def make_table(column):
    """Converts to percentages and prints md table"""
    table_dict = column.value_counts().sort_index().to_dict()
    total = sum(table_dict.values())
    header_str, between_str, count_str = '', '', ''
    for k, v in table_dict.items():
        perc = '%.2f' % round(v / total * 100, 2) + "%"
        header_str += '| ' + k + ' '
        between_str += '| --- '
        count_str += '| ' + perc + ' '
    print(header_str)
    print(between_str)
    print(count_str)

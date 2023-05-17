def make_table(column):
    """Converts to percentages and prints md table"""
    table_dict = column.value_counts().sort_index().to_dict()
    total = sum(table_dict.values())
    first_iteration = True
    for k, v in table_dict.items():
        perc = '%.2f' % round(v / total * 100, 2) + "%"
        if first_iteration:
            header_str = k
            count_str = perc
        else:
            header_str += ' | ' + k
            count_str += ' | ' + perc
        first_iteration = False
    print(header_str)
    print(count_str)

def print_operation_table(operation, num_rows=6, num_columns=6):
    for x in range(num_rows):
        for y in range(num_columns):
            print(operation(x+1, y+1), end=' ')
        print()


print_operation_table(lambda x, y: x * y)

# 36_task

def print_operation_table(operation, num_rows = 6, num_columns = 6):
    a = [[operation(row, col) for col in range(1, num_columns + 1)] for row in range(1, num_rows + 1)]

    for row in a:
        print(*[f"{x:>2}" for x in row])

print_operation_table(lambda x, y: x * y)
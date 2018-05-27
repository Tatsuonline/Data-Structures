""" Write an algorithm such that if an element 
    in an MxN matrix is 0, its entire row and 
    column is set to 0. """

def lelouch (neo):

    zero_column = []
    zero_row = []

    n = len(neo)
    
    for row in neo:
        for column in row:
            if column == 0:
                zero_column.append(row.index(column))
                zero_row.append(neo.index(row))

    for item in zero_row:
        neo[item] = [0] * n

    for item in zero_column:
        for row in range(0, n):
            neo[row][item] = 0

    return print(neo)

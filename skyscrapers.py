'''
Module for checking if the combination on board is winning
'''
def read_input(path: str):
    """
    Read game board file from path.
    Return list of str.

    # >>> read_input("check.txt")
    # ['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***']
    """
    with open(path) as file1:
        table = []
        for line in file1:
            table.append(line[:-1])
        table = table[:-1]
    return table


def left_to_right_check(input_line: str, pivot: int):
    """
    Check row-wise visibility from left to right.
    Return True if number of building from the left-most hint is visible looking to the right,
    False otherwise.

    input_line - representing board row.
    pivot - number on the left-most hint of the input_line.

    >>> left_to_right_check("412453*", 4)
    True
    >>> left_to_right_check("452453*", 5)
    False
    """
    input_line = input_line[1:-1]
    height = '0'
    counter = 5
    for i in range(len(input_line)):
        if input_line[i] > height:
            height = input_line[i]
        else:
            counter -= 1

    if int(counter) != int(pivot):
        return False
    return True



def check_not_finished_board(board: list):
    """
    Check if skyscraper board is not finished, i.e., '?' present on the game board.

    Return True if finished, False otherwise.

    >>> check_not_finished_board(['***21**', '4?????*', '4?????*', '*?????5', \
    '*?????*', '*?????*', '*2*1***'])
    False
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*543215', \
    '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*5?3215', \
    '*35214*', '*41532*', '*2*1***'])
    False
    """
    for elem in board:
        if '?' in elem:
            return False
    return True


def check_uniqueness_in_rows(board: list):
    """
    Check buildings of unique height in each row.

    Return True if buildings in a row have unique length, False otherwise.

    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*543215',\
    '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_uniqueness_in_rows(['***21**', '452453*', '423145*', '*543215', \
    '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*553215', \
    '*35214*', '*41532*', '*2*1***'])
    False
    """
    for i in board[1:-1]:
        i = i[1:-1].replace('*', '')
        if len(set(i))!= len(i):
            return False
    return True




def check_horizontal_visibility(board: list):
    """
    Check row-wise visibility (left-right and vice versa)

    Return True if all horizontal hints are satisfiable,
     i.e., for line 412453* , hint is 4, and 1245 are the four buildings
      that could be observed from the hint looking to the right.

    >>> check_horizontal_visibility(['***21**', '412453*', '423145*', '*543215', \
'*35214*', '*41532*', '*2*1***'])
    True
    >>> check_horizontal_visibility(['***21**', '452453*', '423145*', '*543215', \
'*35214*', '*41532*', '*2*1***'])
    False
    >>> check_horizontal_visibility(['***21**', '452413*', '423145*', '*543215', \
'*35214*', '*41532*', '*2*1***'])
    False
    """
    booleans = []
    for i in board[1:-1]:
        if i[0] != '*':
            pivot = i[0]
            input_line = i
            boolean = left_to_right_check(input_line, pivot)
            booleans.append(boolean)

        if i[-1] != '*':
            pivot = i[-1]
            input_line = i[::-1]

            boolean = left_to_right_check(input_line, pivot)
            booleans.append(boolean)

    return all(booleans)



def check_columns(board: list):
    """
    Check column-wise compliance of the board for uniqueness (buildings of \
    unique height) and visibility (top-bottom and vice versa).

    Same as for horizontal cases, but aggregated in one function for vertical \
    case, i.e. columns.

    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', \
'*41532*', '*2*1***'])
    True
    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', \
'*41232*', '*2*1***'])
    False
    >>> check_columns(['***21**', '412553*', '423145*', '*543215', '*35214*', \
'*41532*', '*2*1***'])
    False
    """
    columns = []
    for i in range(len(board)):
        column = ''
        for row in board:
            column += row[i]
        columns.append(column)

    booleans = [check_uniqueness_in_rows(columns), check_horizontal_visibility(columns)]

    return all(booleans)



def check_skyscrapers(input_path: str):
    """
    Main function to check the status of skyscraper game board.
    Return True if the board status is compliant with the rules,
    False otherwise.

    # >>> check_skyscrapers("check.txt")
    # True
    """
    booleans = []
    board = read_input(input_path)
    booleans.append(check_not_finished_board(board))
    booleans.append(check_uniqueness_in_rows(board))
    booleans.append(check_horizontal_visibility(board))
    booleans.append(check_columns(board))

    return all(booleans)



if __name__ == "__main__":
    print(check_skyscrapers("check.txt"))

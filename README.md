- read_input(path) - Read game board file from path.

- left_to_right_check(input_line: str, pivot: int) -  Check row-wise visibility from left to right.
Return True if number of building from the left-most hint is visible looking to the right,
False otherwise.

- check_not_finished_board(board) - Check if skyscraper board is not finished, i.e., '?' present on the game board.

- check_uniqueness_in_rows(board) - Check buildings of unique height in each row.

- check_horizontal_visibility(board) - Check row-wise visibility (left-right and vice versa)

- check_columns(board) - Check column-wise compliance of the board for uniqueness (buildings of
unique height) and visibility (top-bottom and vice versa).

- check_skyscrapers(input_path) - Main function to check the status of skyscraper game board.
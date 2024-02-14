# Author:  Dominic Fantauzzo
# GitHub username: fantauzd
# Date: 11/07/2023
# Description: Defines a function that solves a puzzle row: Takes a row of numbers and returns True if a token can
# start at the leftmost number and move right/left exactly the amount of that number, eventually reaching the rightmost
# number, which is always 0. The number cannot go outside the row.

def row_puzzle(row):
    """
    Takes a row of numbers and returns True if a token can start at the leftmost number and move right/left exactly the
    amount of that number, eventually reaching the rightmost number, which is always 0. Otherwise, returns False
    The number cannot go outside the row.
    :param row: A list of numbers representing a puzzle
    :return: Boolean value for if the row can be solved
    """
    pos = 0
    memo = []
    return helper_row_puzzle(row, pos, memo)

def helper_row_puzzle(row, pos, memo):
    """
    Helper function for row_puzzle. Uses the pos and memo to track where the token is, and which new moves are still
    possible, respectively. (Returning to old positions does not progress the puzzle so we only consider moves that
    arrive at new valid positions)
    :param row: List of numbers representing a puzzle
    :param pos: The pos of the token
    :param memo: A list of previously visited positions
    :return: Boolean value for if the row can be solved
    """
    if pos == len(row) - 1:  # checks if we reached the end and solved the puzzle
        return True

    memo.append(pos)
    # checks to see if next forward position is new and valid. Moves Token if true
    if pos + row[pos] not in memo and pos + row[pos] <= len(row) - 1:
        return helper_row_puzzle(row, pos + row[pos], memo) and True
    # checks to see if a backward position is new and valid. Moves Token if true and no forward position available.
    if pos - row[pos] not in memo and pos - row[pos] > 0:
        return helper_row_puzzle(row, pos - row[pos], memo) and True

    return False  # returns when no new position possible


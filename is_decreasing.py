# Author:  Dominic Fantauzzo
# GitHub username: fantauzd
# Date: 11/06/2023
# Description: Defines a recursive function that takes as its parameter a list of numbers and returns
# True if the elements of the list are strictly decreasing but returns False otherwise


def is_decreasing(a_list):
    """
    Uses recursion to check if the list is in strictly descending order. Returns True if strictly descending. Returns
    False, otherwise.
    :param a_list: a list of numbers
    :return: Boolean value
    """
    return rec_is_decreasing(a_list)

def rec_is_decreasing(a_list, pos=1, prev=0):
    """
    Helper function for is_decreasing(). Uses recursion to check if the list is in strictly descending order.
    Returns True if strictly descending. Returns False, otherwise.
    :param a_list: a list of numbers
    :param pos: position, must be 1
    :param prev: previous, must be 0
    :return: Boolean value
    """
    if pos == len(a_list): # base case
        return True
    descend = a_list[pos] < a_list[prev]  # True when descending
    return rec_is_decreasing(a_list, pos + 1, prev + 1) and descend  # looks at next two numbers

# Author:  Dominic Fantauzzo
# GitHub username: fantauzd
# Date: 11/06/2023
# Description: Defines a recursive function that takes a list as its parameter and returns the max value within
# the list.

def list_max(a_list):
    """
    Uses recursion to find and return the maximum value from a passed list of numbers
    :param a_list: list of numbers
    :return: the maximum value from a_list
    """
    return rec_list_max(a_list)

def rec_list_max(a_list, pos=0, max_val=None):
    """
    Helper function for list_max. Uses recursion to find and return the maximum value from a passed list of numbers
    :param a_list: list of numbers
    :param pos: initial position must be 0
    :param max_val: initial max must be empty string
    :return:
    """
    if pos == len(a_list):  # base case when we have checked whole list. Big-O(n)
        return max_val
    if max_val == None:  # initialize max_val to first element in list
        max_val = a_list[0]
    if max_val < a_list[pos]:  # update to the smallest value in each recursion
        max_val = a_list[pos]
    return rec_list_max(a_list, pos + 1, max_val)  # increment pos and pass updated max_val


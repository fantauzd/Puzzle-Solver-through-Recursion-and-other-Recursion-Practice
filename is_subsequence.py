# Author:  Dominic Fantauzzo
# GitHub username: fantauzd
# Date: 11/06/2023
# Description: Defines a recursive function that takes two string parameters and returns
# True if the first string is a subsequence of the second string, but returns False otherwise

def is_subsequence(sub, seq):
    """
    Checks if sub is a subsequence of sequence and returns True if it is or False if it is not.
    :param sub: potential subsequence
    :param sequence: string to be checked
    :return: Boolean Value
    """
    return rec_is_subsequence(sub, seq)

def rec_is_subsequence(sub, seq, sub_pos=0, seq_pos =0):
    """
    Helper function for is_subsequence(). Checks if sub is a subsequence of sequence and returns
    True if it is or False if it is not.
    :param sub: potential subsequence
    :param sequence: string to be checked
    :return: Boolean Value
    """
    if sub_pos == len(sub):  # base case for finding all letters in substring
        return True
    if seq_pos == len(seq):  # base case for no moves left and not finding all substring in string
        return False

    if sub[sub_pos] == seq[seq_pos]:  # letter matches
        # move both positions up one (set aside matching letters)
        return rec_is_subsequence(sub, seq, sub_pos + 1, seq_pos + 1)
    if sub[sub_pos] != seq[seq_pos]:  # letter does not match
        # move seq_pos up one to look at next letter
        return rec_is_subsequence(sub, seq, sub_pos, seq_pos + 1)

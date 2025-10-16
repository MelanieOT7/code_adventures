# Todays Challenge 

## Problem Title: Merge Intervals

## Difficulty: Medium

## Problem Statement:
    Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

    Examples:
 
    Example 1:
    Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

    Example 2:
    Input: intervals = [[1,4],[4,5]]
    Output: [[1,5]]
    Explanation: Intervals [1,4] and [4,5] are considered overlapping.
    Constraints:
    •  1 <= intervals.length <= 10^4
    •  intervals[i].length == 2
    •  0 <= start_i <= end_i <= 10^4


# MY approach
    > initialize initial to 0
    loop through the list
    check if first index is greater than initial
        >make list a temporary list
        >add it to new list
    > if not
        append first elemnt of tempo list
        to a list.
        with  second element of the list.
        pop element in the new list
        add a  list to a new list
    > return new list



     

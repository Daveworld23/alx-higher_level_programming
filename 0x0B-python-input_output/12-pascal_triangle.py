#!/usr/bin/python3
"""Defines a pascal's triangle."""


def pascal_triangle(n):
    """Represents the triangle of size n."""
    if n <= 0:
        return []
    """if it is an empty list."""

    first_row = [[1]] #initialize the triangle with row [1]
    for i in range(1, n): #interate fro next row
        new_row = [1] #initialize first elemntbof next row
        for j in range(1, i):
            """calculate for middle values."""
            new_row.append(first_row[i-1][j-1] + first_row[i-1][j]
                    new_row.append(1)
                    first_row.append(new_row)
    return first_row

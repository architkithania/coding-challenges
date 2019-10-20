from typing import Optional, List


def longest_palindrome(string: str) -> str:
    # Generate a matrix where (i, j) True => str[i..j] is Palindrome
    pal_matrix = [[None for i in range(0, len(string))]
                  for j in range(0, len(string))]  # type:List[List[Optional[bool]]] noqa: E501

    # One letter substrings are palindromes
    for i in range(0, len(string)):
        pal_matrix[i][i] = True

    pal_string = ""
    # Check for two letter palindromes
    for i in range(0, len(string) - 1):
        pal_matrix[i][i + 1] = True if string[i] == string[i + 1] else False
        if string[i] == string[i + 1]:
            pal_string == string[i:i + 2]

    # Check for k letter palindromes
    for k in range(3, len(string) + 1):
        for i in range(0, len(string) - k + 1):
            j = i + k - 1
            if string[i] == string[j] and pal_matrix[i - 1][j + 1]:
                pal_matrix[i][j] = True
                pal_string = string[i:j + 1]
            else:
                pal_matrix[i][j] = False

    return pal_string

from collections import Counter


class Solution(object):

  def smallestPalindrome(self, s):
    """:type s: str

    :rtype: str
    """
    counts = Counter(s)

    first_half = []
    middle = ""

    # Process characters in alphabetical order for lexicographically smallest arrangement
    for char in sorted(counts.keys()):
      freq = counts[char]

      # If the frequency is odd, this character forms the middle of the palindrome
      if freq % 2 != 0:
        middle = char

      # Add half of the frequency of the character to the first half
      first_half.append(char * (freq // 2))

    left = "".join(first_half)

    # Combine first half, middle character (if any), and reversed first half
    return left + middle + left[::-1]
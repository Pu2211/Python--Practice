class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        n = len(word)
        pushes = 0
        
        # There are 8 available keypad keys (2 through 9).
        # The first 8 letters require 1 push each.
        # The next 8 letters require 2 pushes each, and so on.
        for i in range(n):
            pushes += (i // 8) + 1
            
        return pushes
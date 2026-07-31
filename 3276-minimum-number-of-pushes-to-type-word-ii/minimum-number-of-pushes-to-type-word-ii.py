from collections import Counter

class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        # Step 1: Count character frequencies in word
        counts = Counter(word)
        
        # Step 2: Sort frequencies in descending order
        sorted_freqs = sorted(counts.values(), reverse=True)
        
        # Step 3: Greedily map the most frequent characters to 1 push, next to 2 pushes, etc.
        pushes = 0
        for i, freq in enumerate(sorted_freqs):
            pushes += freq * ((i // 8) + 1)
            
        return pushes